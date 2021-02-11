# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class university(models.Model):
#     _name = 'university.university'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

# -*- coding: utf-8 -*-
from odoo import models, fields


class UniversityStudent(models.Model):
    _name = 'university.student'
    _rec_name = "f_name"
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    inscription_date = fields.Datetime('Date of Inscription')
    email = fields.Char()
    phone = fields.Char()

    departement_id = fields.Many2one(comodel_name='university.departement')
    classroom_id = fields.Many2one(comodel_name='university.classroom')
    subject_ids = fields.Many2many(related='classroom_id.subject_ids')

    def name_get(self):
        result = []

        for student in self:
            name = '[' + student.classroom_id.classroom_name + ']' + student.f_name + ' ' + student.l_name
            result.append((student.id, name))
            return result
