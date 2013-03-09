# coding: utf-8
import mock
import datetime

from contextlib import contextmanager

from dext.utils import s11n

from textgen.words import Noun

from game.balance.enums import RACE

from game.bills.prototypes import BillPrototype
from game.bills import bills
from game.bills.tests.prototype_tests import BaseTestPrototypes

from game.chronicle.models import Record, RECORD_TYPE

from game.map.places.modifiers import TradeCenter, CraftCenter

@contextmanager
def check_record_created(self, record_type, records_number=1):
    old_records_number = Record.objects.all().count()

    yield

    self.assertEqual(old_records_number + records_number, Record.objects.all().count())
    self.assertEqual(Record.objects.all().order_by('-id')[0].type, record_type)

@mock.patch('game.bills.prototypes.BillPrototype.time_before_end_step', datetime.timedelta(seconds=0))
def process_bill(bill, success):
    with mock.patch('game.bills.prototypes.BillPrototype.is_percents_barier_not_passed', not success):
        with mock.patch('game.bills.prototypes.BillPrototype.is_votes_barier_not_passed', not success):
            bill.apply()

class BillPlaceRenamingTests(BaseTestPrototypes):

    def setUp(self):
        super(BillPlaceRenamingTests, self).setUp()

        bill_data = bills.PlaceRenaming(place_id=self.place1.id, base_name='new-name')
        self.bill = BillPrototype.create(self.account1, 'bill-caption', 'bill-rationale', bill_data)

        noun = Noun.fast_construct(self.bill.data.base_name)
        self.form = bills.PlaceRenaming.ModeratorForm({'approved': True,
                                                       'name_forms': s11n.to_json(noun.serialize()) })
        self.assertTrue(self.form.is_valid())


    def test_bill_started(self):

        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_NAME_BILL_STARTED):
            self.bill.update_by_moderator(self.form)

    def test_bill_successed(self):
        self.bill.update_by_moderator(self.form)
        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_NAME_BILL_SUCCESSED):
            process_bill(self.bill, True)

    def test_bill_failed(self):
        self.bill.update_by_moderator(self.form)
        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_NAME_BILL_FAILED):
            process_bill(self.bill, False)


class BillPlaceDescriptionTests(BaseTestPrototypes):

    def setUp(self):
        super(BillPlaceDescriptionTests, self).setUp()

        bill_data = bills.PlaceDescripton(place_id=self.place1.id, description='new description')
        self.bill = BillPrototype.create(self.account1, 'bill-1-caption', 'bill-1-rationale', bill_data)

        self.form = bills.PlaceDescripton.ModeratorForm({'approved': True})
        self.assertTrue(self.form.is_valid())

    def test_bill_started(self):

        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_DESCRIPTION_BILL_STARTED):
            self.bill.update_by_moderator(self.form)

    def test_bill_successed(self):
        self.bill.update_by_moderator(self.form)
        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_DESCRIPTION_BILL_SUCCESSED):
            process_bill(self.bill, True)

    def test_bill_failed(self):
        self.bill.update_by_moderator(self.form)
        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_DESCRIPTION_BILL_FAILED):
            process_bill(self.bill, False)


class BillPlaceChangeModifierTests(BaseTestPrototypes):

    def setUp(self):
        super(BillPlaceChangeModifierTests, self).setUp()

        bill_data = bills.PlaceModifier(place_id=self.place1.id, modifier_id=TradeCenter.get_id(), modifier_name=TradeCenter.NAME, old_modifier_name=None)
        self.bill = BillPrototype.create(self.account1, 'bill-1-caption', 'bill-1-rationale', bill_data)

        self.form = bills.PlaceDescripton.ModeratorForm({'approved': True})
        self.assertTrue(self.form.is_valid())

    def test_bill_started(self):
        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_MODIFIER_BILL_STARTED):
            self.bill.update_by_moderator(self.form)

    def test_bill_successed(self):
        self.bill.update_by_moderator(self.form)
        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_MODIFIER_BILL_SUCCESSED):
            process_bill(self.bill, True)

    def test_bill_failed(self):
        self.bill.update_by_moderator(self.form)
        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_MODIFIER_BILL_FAILED):
            process_bill(self.bill, False)

class BillPersonRemoveTests(BaseTestPrototypes):

    def setUp(self):
        super(BillPersonRemoveTests, self).setUp()

        bill_data = bills.PersonRemove(person_id=self.place1.persons[0].id, old_place_name_forms=self.place1.normalized_name)
        self.bill = BillPrototype.create(self.account1, 'bill-1-caption', 'bill-1-rationale', bill_data)

        self.form = bills.PlaceDescripton.ModeratorForm({'approved': True})
        self.assertTrue(self.form.is_valid())

    def test_bill_started(self):
        with check_record_created(self, RECORD_TYPE.PERSON_REMOVE_BILL_STARTED):
            self.bill.update_by_moderator(self.form)

    @mock.patch('game.chronicle.records.PlaceChangeRace.create_record', lambda x: None)
    @mock.patch('game.chronicle.records.PersonArrivedToPlace.create_record', lambda x: None)
    def test_bill_successed(self):
        self.bill.update_by_moderator(self.form)
        with check_record_created(self, RECORD_TYPE.PERSON_REMOVE_BILL_SUCCESSED):
            process_bill(self.bill, True)

    def test_bill_failed(self):
        self.bill.update_by_moderator(self.form)
        with check_record_created(self, RECORD_TYPE.PERSON_REMOVE_BILL_FAILED):
            process_bill(self.bill, False)


class PlaceLosedModifierTests(BaseTestPrototypes):

    def setUp(self):
        super(PlaceLosedModifierTests, self).setUp()

        self.place1.modifier = CraftCenter.get_id()
        self.place1.save()

    @mock.patch('game.map.places.modifiers.prototypes.CraftCenter.is_enough_power', False)
    def test_reset_modifier(self):
        with check_record_created(self, RECORD_TYPE.PLACE_LOSED_MODIFIER):
            self.place1.sync_modifier()


class PersonMovementsTests(BaseTestPrototypes):

    def setUp(self):
        super(PersonMovementsTests, self).setUp()

    @mock.patch('game.persons.prototypes.PersonPrototype.is_stable', False)
    @mock.patch('game.map.places.prototypes.PlacePrototype.max_persons_number', 0)
    def test_person_left(self):
        with check_record_created(self, RECORD_TYPE.PERSON_LEFT_PLACE, records_number=len(self.place1.persons)):
            self.place1.sync_persons()

    @mock.patch('game.chronicle.records.PlaceChangeRace.create_record', lambda x: None)
    def test_person_arrived(self):
        with check_record_created(self, RECORD_TYPE.PERSON_ARRIVED_TO_PLACE):
            with mock.patch('game.map.places.prototypes.PlacePrototype.max_persons_number', len(self.place1.persons) + 1):
                self.place1.sync_persons()


class PlaceChangeRace(BaseTestPrototypes):

    def setUp(self):
        super(PlaceChangeRace, self).setUp()

        for race_id in RACE._ALL:
            if self.place1.race != race_id:
                self.next_race_id = race_id

    def test_place_race_changed(self):
        for person in self.place1.persons:
            person._model.race = self.next_race_id
            person.save()

        with check_record_created(self, RECORD_TYPE.PLACE_CHANGE_RACE):
            self.place1.sync_race()