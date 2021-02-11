# -*- coding: utf-8 -*-
from odoo import models, fields


class UniversityProfessor(models.Model):
    _name = 'university.professor'
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    start = fields.Datetime('StartDate')
    email = fields.Char()
    phone = fields.Char()
    departement_id = fields.Many2one(comodel_name='university.departement')
    subject_id = fields.Many2one(comodel_name='university.subject')
    classroom_ids = fields.Many2many(comodel_name='university.classroom', relation='prof_class_rel', column1='f_name',
                                     column2='name')
