# -*- coding: utf-8 -*-
from odoo import models, fields, api
import uuid

from odoo.exceptions import ValidationError


class SportClubReview(models.Model):
    _name = 'sportclub.review'
    _rec_name = 'reviewer_name'
    code = fields.Char(compute='getuniqueid')
    score = fields.Float(required=True)
    description = fields.Text()
    creaation_date = fields.Datetime('creation date', default=fields.Date.today)
    sportclub_id = fields.Many2one(comodel_name='sportclub.sportclub')

    player_id = fields.Many2one(comodel_name='sportclub.player')

    reviewer_name = fields.Char(compute='get_reviewer_name', default="User")

    def get_reviewer_name(self):
        self.reviewer_name = str(self.player_id.fullname) + ' review '

    def getuniqueid(self):
        self.code = uuid.uuid1()

    @api.constrains('score')
    def _check_value(self):
        if 0 >= self.score > 10:
            raise ValidationError('surface needs to be positive')
