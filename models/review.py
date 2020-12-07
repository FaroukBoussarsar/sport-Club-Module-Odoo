# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubReview(models.Model):
    _name = 'sportclub.review'

    code = fields.Char()
    score = fields.Float()
    description = fields.Text()
    creaation_date = fields.Datetime('creation date')
