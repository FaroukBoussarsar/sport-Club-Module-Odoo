# -*- coding: utf-8 -*-
from odoo import models, fields


class UniversityDepartement(models.Model):
    _name = 'university.departement'
    name = fields.Char()
    code = fields.Char()
    professor_ids = fields.One2many(comodel_name='university.professor', inverse_name='departement_id')
    subject_ids = fields.One2many(comodel_name='university.subject', inverse_name='departement_id')
