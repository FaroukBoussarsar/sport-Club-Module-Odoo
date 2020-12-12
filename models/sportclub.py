# -*- coding: utf-8 -*-


from odoo import models, fields, api

import uuid

from odoo.exceptions import ValidationError


class SportClub(models.Model):
    _name = 'sportclub.sportclub'
    _rec_name = 'sportclub_name'
    sportclub_name = fields.Char(String='name', required=True)
    code_sportclub = fields.Char(compute='getuniqueid')
    creaation_date = fields.Datetime('creation date', required=True)
    surface = fields.Float(required=True)
    owner_id = fields.Many2one(comodel_name='sportclub.owner', readonly=True)
    # stadium_ids = fields.One2many(comodel_name='sportclub.stadium', inverse_name='sportclub_id', required=True)
    review_ids = fields.One2many(comodel_name='sportclub.review', inverse_name='sportclub_id')
    stadium_ids = fields.Many2many(comodel_name='sportclub.stadium', relation='class_sport_stad',
                                   column1='sportclub_name',
                                   column2='stadium_name')
    def getuniqueid(self):
        self.code_sportclub = uuid.uuid1()


    @api.constrains('surface')
    def _check_value(self):
        if self.surface <= 0:
            raise ValidationError('surface needs to be positive')