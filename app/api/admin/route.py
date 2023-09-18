from flask import Blueprint

admin_api = Blueprint("admin_api", __name__, url_prefix="/admin")

from .item.route import item_api

admin_api.register_blueprint(item_api)

from .coupon.route import coupon_api

admin_api.register_blueprint(coupon_api)

from .pool.route import pool_api

admin_api.register_blueprint(pool_api)
