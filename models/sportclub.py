# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClub(models.Model):
    _name = 'sportclub.sportclub'
    _rec_name = 'sportclub_name'
    sportclub_name = fields.Char(String='name')
    code = fields.Char()
    creaation_date = fields.Datetime('creation date')
    surface = fields.Float()
    owner_id = fields.Many2one(comodel_name='sportclub.owner')
    stadium_ids = fields.One2many(comodel_name='sportclub.stadium', inverse_name='sportclub_id')
    review_ids = fields.One2many(comodel_name='sportclub.review', inverse_name='sportclub_id')