# -*- coding: utf-8 -*-
from odoo import models, fields


class UniversityClassRoom(models.Model):
    _name = 'university.classroom'
    classroom_name = fields.Char(String='name')
    code = fields.Char()

    student_ids = fields.One2many(comodel_name='university.student', inverse_name='classroom_id')

    professor_ids = fields.Many2many(comodel_name='university.professor', relation='class_prof_rel',
                                     column1='name',
                                     column2='f_name')

    subject_ids = fields.Many2many(comodel_name='university.subject', relation='class_sub_rel',
                                   column1='classroom_name',
                                   column2='name')

    num_prof = fields.Integer(String="number of professors",
                              compute='comp_prof')
    num_sub = fields.Integer(String="number of subjects", compute='comp_sub')
    num_stu = fields.Integer(String="number de students", compute='comp_stu')

    def comp_prof(self):
        self.num_prof = len(self.professor_ids)

    def comp_sub(self):
        self.num_prof = len(self.subject_ids)

    def comp_stu(self):
        self.num_prof = len(self.student_ids)
