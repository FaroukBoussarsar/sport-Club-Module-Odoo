# -*- coding: utf-8 -*-
from odoo import models, fields
import uuid

class SportClubReview(models.Model):
    _name = 'sportclub.review'
    _rec_name = 'reviewer_name'
    code = fields.Char(compute='getuniqueid')
    score = fields.Float(required=True)
    description = fields.Text()
    creaation_date = fields.Datetime('creation date', default=fields.Datetime.today)
    sportclub_id = fields.Many2one(comodel_name='sportclub.sportclub')

    player_id = fields.Many2one(comodel_name='sportclub.player')

    reviewer_name = fields.Char(compute='get_reviewer_name')

    def get_reviewer_name(self):
        self.reviewer_name = str(self.player_id.fullname) + ' review '

    def getuniqueid(self):
        self.code = uuid.uuid1()
