##############################################################################
#
#    Copyright (C) 2022-Present Speeduplight (<https://speeduplight.com>)
#
##############################################################################
{
    "name": "Create Sales Quatation From pos | pos create sale order In Odoo | Scan Products And create sale order From pos | Point Of Sale sale order Creation",
    "version": "16.0.1",
    'sequence': -10,
    "category": "Sales/Point of Sale",
    'license': 'OPL-1',
    "author": "Speeduplight",
    "description": """Create odoo sales quotation from point of sale, create new sales order from pos, pos sales order creation,
        pos sale order , quotation create from pos, sale order create from pos , create order from pos pos sale order create , create sale quotation from pos , sale quotation create from pos , pos sale quotation create , quotation create pos , sale create from pos , sale order pos , quotation order pos
        sales quotation creation from pos, odoo create sales order from point of sale create sale from pos, pos save quotation,
        create SO from pos create sales from point of sale add quotation form pos create quotation from pont of sale 
        point of sales create sales from pos generate sales order from pos add quotation from pos create sales order from pos
        create quotation sale order from point of sale create quotation from point of sale, create sale order from pos
        create sale order from point of sale sale order from pos, sale order of pos order create SO from pos order from pos,
        odoo create sale order from point of sale create Sale from point of sale, create quotation sale order from pos
        odoo create sale order from point of sale create SO from pos create sales from pont of sale
        odoo add quotation form pos create quotation from pont of sale odoo create Sales from pos Generate sales order from pos
        odoo add quotation from pos create sales order from pos odoo import sale order from point of sale import Sale from point of sale
        odoo import Sales from point of sale import SO from pos odoo Import SO from point of sale import sales from point of sale
        odoo Import sale order from pos import quotation form pos odoo import quotation from pont of sale import Sales from pos
        odoo import sales order from pos import quotation from pos, odoo import sales order from pos odoo import quote from pos odoo import quote from point of sale
        odoo point of sale save quotation point of sale add quotation point of sale create quotation odoo odoo point of sales save quotation point of sales add quotation point of sales create quotation odoo
        odoo pos save quotation pos add quotation pos create quotation odoo""",
    'summary': """Create odoo sales quotation from point of sale, create new sales order from pos, pos sales order creation, 
        pos sale order , quotation create from pos, sale order create from pos , create order from pos
        sales quotation creation from pos, odoo create sales order from point of sale create sale from pos, pos save quotation,
        create SO from pos create sales from point of sale add quotation form pos create quotation from pont of sale 
        point of sales create sales from pos generate sales order from pos add quotation from pos create sales order from pos
        create quotation sale order from point of sale create quotation from point of sale, create sale order from pos
        create sale order from point of sale sale order from pos, sale order of pos order create SO from pos order from pos,
        odoo create sale order from point of sale create Sale from point of sale, create quotation sale order from pos
        odoo create sale order from point of sale create SO from pos create sales from pont of sale
        odoo add quotation form pos create quotation from pont of sale odoo create Sales from pos Generate sales order from pos
        odoo add quotation from pos create sales order from pos odoo import sale order from point of sale import Sale from point of sale
        odoo import Sales from point of sale import SO from pos odoo Import SO from point of sale import sales from point of sale
        odoo Import sale order from pos import quotation form pos odoo import quotation from pont of sale import Sales from pos
        odoo import sales order from pos import quotation from pos, odoo import sales order from pos odoo import quote from pos odoo import quote from point of sale
        odoo point of sale save quotation point of sale add quotation point of sale create quotation odoo odoo point of sales save quotation point of sales add quotation point of sales create quotation odoo
        odoo pos save quotation pos add quotation pos create quotation odoo""",
    "website": "https://speeduplight.com",
    "depends": ['base', 'sale_management', 'point_of_sale'],
    "data": [],
    'assets': {
        'point_of_sale.assets': [
            'sp_create_sale_order_in_pos/static/src/js/MakeSalesOrderButton.js',
            'sp_create_sale_order_in_pos/static/src/xml/make_order.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 10,
    'currency': 'USD',
    'images': ['static/description/pos_banner.gif']
}
