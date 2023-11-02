import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'kw.lib.auth'
    _description = 'Author'

    name = fields.Char()

    _active = fields.Boolean(
        default=True, )
