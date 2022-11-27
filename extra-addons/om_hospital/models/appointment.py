from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"  # odoo will create table hospital_patient in the db
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"

    patient_id = fields.Many2one(
        comodel_name='hospital.patient', string="Patient")
    appointment_time = fields.Datetime(string='Appointment Time')
    booking_date = fields.Date(string='Booking Date')