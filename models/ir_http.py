import logging

from odoo import models
from odoo.http import request

_logger = logging.getLogger(__name__)

# Country code -> Odoo language code
COUNTRY_LANG_MAP = {
    'SE': 'sv_SE',
    'NO': 'nb_NO',
}
DEFAULT_LANG_CODE = 'en_US'


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _get_default_lang(cls):
        """Return a GeoIP-based language for first-time visitors.

        Only takes effect when no URL lang, cookie, or context lang is set.
        Falls back to the website's configured default if GeoIP is unavailable
        or the target language is not installed on the website.
        """
        try:
            country_code = request.geoip.country_code
        except Exception:
            return super()._get_default_lang()

        if not country_code:
            return super()._get_default_lang()

        lang_code = COUNTRY_LANG_MAP.get(country_code, DEFAULT_LANG_CODE)
        nearest = request.env['ir.http'].get_nearest_lang(lang_code)

        if nearest:
            return request.env['res.lang']._get_data(code=nearest)

        return super()._get_default_lang()
