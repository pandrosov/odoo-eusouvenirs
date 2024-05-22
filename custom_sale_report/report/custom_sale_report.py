from odoo import models, api

class ReportCustomSaleOrder(models.AbstractModel):
    _name = 'report.custom_sale_report.custom_sale_report_template'
    _description = 'Custom Sale Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['sale.order'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': docs,
        }
