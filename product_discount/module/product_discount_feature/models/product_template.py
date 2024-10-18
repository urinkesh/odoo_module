from odoo import _, api, fields, models

class product_template(models.Model):
    _inherit = 'product.template'

    discount_percentage = fields.Float('Discount (%)')
    

    def _get_sales_prices(self, pricelist):
        res = super(product_template, self)._get_sales_prices(pricelist)
        for product_template_id in res:
            product_template_id = self.browse(product_template_id) 
            if product_template_id.discount_percentage:
                price =res[product_template_id.id].get('price_reduce')
                discount_price =  price -((price * product_template_id.discount_percentage) / 100)
                res[product_template_id.id].update({
                    'price_reduce' : discount_price,
                    'base_price' : price,
                })
        return res
        
    
    def _get_combination_info(self, combination=False, product_id=False, add_qty=1, pricelist=False, parent_combination=False, only_template=False):
        res = super(product_template, self)._get_combination_info(
            combination=combination, product_id=product_id, add_qty=add_qty, pricelist=pricelist,
            parent_combination=parent_combination, only_template=only_template)
        product_template_id = self or  self.env['product.product'].browse(product_id).product_tmpl_id
        if product_template_id.discount_percentage:
            price = res.get('price',0)
            list_price = res.get('list_price',0)
            discount_price =  price -((price * product_template_id.discount_percentage) /100)        
            res.update({
                'price' : discount_price,
                'list_price' : list_price,
                'compare_list_price' : price,
                'group_product_price_comparison' : self.env.user.has_group('website_sale.group_product_price_comparison')
            })
        return res