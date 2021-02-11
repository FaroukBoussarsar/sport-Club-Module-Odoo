# -*- coding: utf-8 -*-
from odoo import models, fields


class UniversitySubject(models.Model):
    _name = 'university.subject'
    name = fields.Char()
    code = fields.Char()
    departement_id = fields.Many2one(comodel_name='university.departement')
    professor_ids = fields.Many2many(comodel_name='university.professor',
                                     relation='sub_prof_rel',
                                     column1='name',
                                     column2='f_name')
