from odoo import _, api, fields, models

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('product_id', 'product_uom', 'product_uom_qty')
    def _compute_discount(self):
        super(sale_order_line, self)._compute_discount()
        for line in self:
            if line.product_id and line.product_id.product_tmpl_id.discount_percentage :
                line.discount = line.product_id.product_tmpl_id.discount_percentage
        