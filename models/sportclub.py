# -*- coding: utf-8 -*-
from odoo import models, fields

import uuid


class SportClub(models.Model):
    _name = 'sportclub.sportclub'
    _rec_name = 'sportclub_name'
    sportclub_name = fields.Char(String='name', required=True)
    code = fields.Char(compute='getuniqueid')
    creaation_date = fields.Datetime('creation date', required=True)
    surface = fields.Float(equired=True)
    owner_id = fields.Many2one(comodel_name='sportclub.owner')
    stadium_ids = fields.One2many(comodel_name='sportclub.stadium', inverse_name='sportclub_id', required=True)
    review_ids = fields.One2many(comodel_name='sportclub.review', inverse_name='sportclub_id')

    def getuniqueid(self):
        self.code = uuid.uuid1()
