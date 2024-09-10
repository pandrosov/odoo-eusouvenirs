##############################################################################
#
#    Copyright (C) 2022-Present Speeduplight (<https://speeduplight.com>)
#
##############################################################################
from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def make_sales_order(self, partner_id, orderlines, cashier_id, config_id):
        sale_object = self.env['sale.order']
        sale_order_line_obj = self.env['sale.order.line']
        warehouse = False
        if config_id:
            pos_config_rec = self.env['pos.config'].sudo().browse(config_id.get('id'))
            if pos_config_rec and pos_config_rec.picking_type_id and pos_config_rec.picking_type_id.warehouse_id:
                warehouse = pos_config_rec.picking_type_id.warehouse_id or False
        order_id = sale_object.create({
            'partner_id': partner_id,
            'user_id': cashier_id,
            'warehouse_id': warehouse.id,
        })

        for dict_line in orderlines:
            product_obj = self.env['product.product']
            product_dict = dict_line.get('product')
            product_tax = product_obj.browse(product_dict.get('id'))
            tax_ids = []
            for tax in product_tax.taxes_id:
                tax_ids.append(tax.id)
            product_id = product_obj.browse(product_dict.get('id'))
            vals = {'product_id': product_dict.get('id'),
                    'name': product_id.display_name,
                    'product_uom_qty': product_dict.get('quantity'),
                    'price_unit': product_dict.get('price'),
                    'product_uom': product_dict.get('uom_id'),
                    'tax_id': [(6, 0, tax_ids)],
                    'discount': product_dict.get('discount'),
                    'order_id': order_id.id}
            sale_order_line_obj.create(vals)
        return order_id.name
