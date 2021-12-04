from django.test import TestCase
from django.contrib.auth.models import User 
from task2_main.models import VoltageSensor, Measurement
from django.db import IntegrityError
from datetime import datetime

class TestMeasurementModel(TestCase):
    fixtures = ['test_fixtures.yaml']
    sensor=None
    time_stamp=datetime.strptime('19:00', "%H:%M")
    current_voltage=1
    is_error=False

    def setUp(self):
        self.user=User.objects.get(pk=1)
        self.sensor= VoltageSensor.objects.get(pk=1)

    def create_test_measurement_with_user(self, user_obj: User= None) -> VoltageSensor:
        return Measurement.objects.create(
            sensor=user_obj,
            time_stamp=self.time_stamp,
            current_voltage=self.current_voltage,
            is_error=self.is_error,

        )

    def create_test_measurement_with_voltagesensor(self, voltage_sensor_obj: VoltageSensor = None) -> Measurement:
        return Measurement.objects.create(
            sensor=voltage_sensor_obj,
            time_stamp=self.time_stamp,
            current_voltage=self.current_voltage,
            is_error=self.is_error,

        )

    def test_can_not_create_empty_measurement(self):
        with self.assertRaises(IntegrityError):
            Measurement.objects.create()

    def test_can_not_create_booking_without_user(self):
        with self.assertRaises(IntegrityError):
            self.create_test_measurement_with_user

    def test_can_not_create_booking_without_service(self):
        with self.assertRaises(IntegrityError):
            self.create_test_measurement_with_voltagesensor()

    def test_can_create_measurement_with_test_data(self):
        measurement_obj = self.create_test_measurement_with_user(self.user)
        self.assertEqual(measurement_obj.is_error, self.is_error)
        self.assertEqual(measurement_obj.current_voltage, self.current_voltage)
        self.assertEqual(measurement_obj.time_stamp, self.time_stamp)
        self.assertEqual(measurement_obj.sensor, self.sensor)


