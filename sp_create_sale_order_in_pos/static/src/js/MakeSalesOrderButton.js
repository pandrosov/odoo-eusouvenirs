odoo.define('sp_create_sale_order_in_pos.MakeSalesOrderButton', function(require) {
	'use strict';

	const PosComponent = require('point_of_sale.PosComponent');
	const ProductScreen = require('point_of_sale.ProductScreen');
	const { useListener } = require("@web/core/utils/hooks");
	const Registries = require('point_of_sale.Registries');


	class MakeSalesOrderButton extends PosComponent {
		setup() {
			super.setup();
			useListener('click', this.onClick);
		}
			
		async onClick(){
			var self = this;
			var order = self.env.pos.get_order();
			var orderlines = order.orderlines;
			var cashier_id = self.env.pos.get_cashier().id;
			var partner_id = false;
			var pos_product_list = [];
			var config = self.env.pos.config;

			if (order.get_partner() != null)
				partner_id = order.get_partner().id;

			if (!partner_id) {
				return self.showPopup('ErrorPopup', {
					title: self.env._t('Unknown customer'),
					body: self.env._t('You cannot Create Sales Order. Select customer first.'),
				});
			}

			if (orderlines.length === 0) {
				return self.showPopup('ErrorPopup', {
					title: self.env._t('Empty Order'),
					body: self.env._t('There must be at least one product in your order before Add a note.'),
				});
			}

			for (var i = 0; i < orderlines.length; i++) {
				var product_items = {
					'id': orderlines[i].product.id,
					'quantity': orderlines[i].quantity,
					'uom_id': orderlines[i].product.uom_id[0],
					'price': orderlines[i].price,
					'discount': orderlines[i].discount,
					'is_lot': orderlines[i].has_product_lot,
				};
				pos_product_list.push({'product': product_items });
			}

			self.rpc({
				model: 'sale.order',
				method: 'make_sales_order',
				args: [partner_id, partner_id, pos_product_list, cashier_id, config],
			}).then(function(output) {
				self.showPopup('ConfirmPopup', {
                    title: self.env._t('Sale Order created!'),
                    body: self.env._t(output),
                });
                if(orderlines.length > 0){
                    var lines_count = orderlines.length;
                    while(lines_count){
                        order.remove_orderline(orderlines[0]);
                        lines_count = orderlines.length;
                    }
				}
				order.set_partner(false);
			});
		}
	}

	MakeSalesOrderButton.template = 'MakeSalesOrderButton';
	ProductScreen.addControlButton({
		component: MakeSalesOrderButton,
		position: ['before', 'SetPricelistButton'],
	});
	Registries.Component.add(MakeSalesOrderButton);
	return MakeSalesOrderButton;
});