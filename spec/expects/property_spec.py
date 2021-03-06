# -*- coding: utf-8 -*-

from mamba import describe, context, before

from spec.fixtures import Foo

from expects import expect
from expects.testing import failure


with describe('property') as _:
    def it_should_pass_if_actual_has_property():
        expect(_.obj).to.have.property('bar')

    def it_should_pass_if_actual_has_property_with_value():
        expect(_.obj).to.have.property('bar', 0)

    def it_should_fail_if_actual_does_not_have_property():
        with failure(_.obj, "to have property 'foo'"):
            expect(_.obj).to.have.property('foo')

    def it_should_fail_if_actual_hasnt_property_with_value():
        with failure(_.obj, "to have property 'foo'"):
            expect(_.obj).to.have.property('foo', 0)

    def it_should_fail_if_actual_has_property_without_value():
        with failure(_.obj, "to have property 'bar' with value 1 but was 0"):
            expect(_.obj).to.have.property('bar', 1)

    def it_should_fail_if_actual_has_property_without_none_value():
        with failure(_.obj, "to have property 'bar' with value None but was 0"):
            expect(_.obj).to.have.property('bar', None)

    with context('#negated'):
        def it_should_pass_if_actual_does_not_have_property():
            expect(_.obj).not_to.have.property('foo')

        def it_should_pass_if_actual_does_not_have_property_with_value():
            expect(_.obj).not_to.have.property('foo', 0)

        def it_should_pass_if_actual_has_property_without_value():
            expect(_.obj).not_to.have.property('bar', 1)

        def it_should_fail_if_actual_has_property():
            with failure(_.obj, "not to have property 'bar'"):
                expect(_.obj).not_to.have.property('bar')

        def it_should_fail_if_actual_has_property_with_value():
            with failure(_.obj, "not to have property 'bar' with value 0 but was 0"):
                expect(_.obj).not_to.have.property('bar', 0)

    with context('#chain'):
        def it_should_pass_if_actual_has_property_with_value_equal():
            expect(_.obj).to.have.property('bar').with_value.equal(0)

        def it_should_pass_if_actual_has_property_with_value_not_equal():
            expect(_.obj).to.have.property('bar').with_value.not_equal(1)

        def it_should_fail_if_actual_has_property_without_value_equal():
            with failure(_.obj, "to have property 'bar' with value 0 equal 1"):
                expect(_.obj).to.have.property('bar').with_value.equal(1)

        def it_should_fail_if_actual_has_property_without_value_not_equal():
            with failure(_.obj, "to have property 'bar' with value 0 not equal 0"):
                expect(_.obj).to.have.property('bar').with_value.not_equal(0)

        def it_should_return_none_if_value_passed():
            expect(expect(_.obj).to.have.property('bar', 0)).to.be.none

    @before.each
    def fixtures():
        _.obj = Foo()
