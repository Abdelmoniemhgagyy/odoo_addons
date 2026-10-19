/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ListController } from "@web/views/list/list_controller";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { user } from "@web/core/user";
import { exprToBoolean } from "@web/core/utils/strings";
import { STATIC_ACTIONS_GROUP_NUMBER } from "@web/search/action_menus/action_menus";
import { useBus } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { evaluateBooleanExpr } from "@web/core/py_js/py";

const cogMenuRegistry = registry.category("cogMenu");

patch(ListController.prototype, {
    setup() {
        super.setup();
        useBus(this.env.searchModel, "print-pdf-all", () => this.onPrintPDF());
    },

    /**
     * @override
     */
    getStaticActionMenuItems() {
        const items = super.getStaticActionMenuItems();
        if (this.isExportEnable) {
            items.print_pdf = {
                sequence: 15,
                icon: "fa fa-print",
                description: _t("Print PDF"),
                callback: () => this.onPrintPDF(),
            };
        }
        return items;
    },

    async onPrintPDF() {
        const model = this.model.root.resModel;
        const domain = this.model.root.domain;
        const resIds = this.model.root.selection.map((r) => r.resId);
        
        // Match Odoo's export field selection logic
        const fields = this.props.archInfo.columns
            .filter((col) => col.type === "field")
            .filter((col) => !col.optional || this.optionalActiveFields[col.name])
            .filter((col) => !evaluateBooleanExpr(col.column_invisible, this.props.context))
            .filter((col) => this.props.fields[col.name].exportable !== false)
            .map((col) => {
                const field = this.props.fields[col.name];
                return {
                    name: col.name,
                    label: col.label || col.string || field.string,
                    aggregate: col.sum ? 'sum' : (col.avg ? 'avg' : null),
                };
            });

        const action = {
            type: "ir.actions.report",
            report_name: "asl_list_view_pdf_print.report_list_view",
            report_type: "qweb-pdf",
            data: {
                model: model,
                domain: domain,
                fields: fields,
                groupby: this.model.root.groupBy,
                title: this.props.title || model,
                res_ids: resIds,
            },
            context: this.props.context,
        };

        return this.actionService.doAction(action);
    },
});

/**
 * 'Print PDF All' menu component for Cog Menu
 */
export class PrintPDFAll extends Component {
    static template = "asl_list_view_pdf_print.PrintPDFAll";
    static components = { DropdownItem };

    async onPrintAll() {
        this.env.searchModel.trigger("print-pdf-all");
    }
}

cogMenuRegistry.add("print-pdf-all-menu", {
    Component: PrintPDFAll,
    groupNumber: STATIC_ACTIONS_GROUP_NUMBER,
    isDisplayed: async (env) =>
        env.config.viewType === "list" &&
        !env.model.root.selection.length &&
        (await user.hasGroup("base.group_allow_export")) &&
        exprToBoolean(env.config.viewArch.getAttribute("export_xlsx"), true),
}, { sequence: 15 });
