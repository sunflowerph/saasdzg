import Basic_Operations
from robot.api.deco import keyword


#添加商品
@keyword("Add Product")
def add_product(product_name):
    return Basic_Operations.add_product(product_name)

#商品入库
@keyword("Product Storage")
def product_storage():
    return Basic_Operations.product_storage()


#销售出库
@keyword('Sale')
def sale():
    return Basic_Operations.sale()

#获取库存数据
@keyword('Get Inventory')
def get_inventory():
    return Basic_Operations.get_inventory()
