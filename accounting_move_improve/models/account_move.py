# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveImprove(models.Model):
    _inherit = 'account.move'

    documents = fields.Many2many('ir.attachment', String='Attachments')