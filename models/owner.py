# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from odoo import models, fields


class SportClubOwner(models.Model):
    _name = 'sportclub.owner'
    f_name = fields.Char('first name')
    l_name = fields.Char('last name')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    birthday = fields.Date('Birthday')
    address = fields.Text('Address')
    email = fields.Char('email')
    phone = fields.Char('phone number')
  #  departement_id = fields.Many2one(comodel_name='university.departement')
  #  subject_id = fields.Many2one(comodel_name='university.subject')
  #  classroom_ids = fields.Many2many(comodel_name='university.classroom', relation='prof_class_rel', column1='f_name',
      #                               column2='name')
