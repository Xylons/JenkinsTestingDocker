#!/usr/bin/env python3
"""
Unit tests for the calculator program
"""

import calculator


class Tests:

    def test_mult(self):
        assert 25 == calculator.mult(5,5)
        
    def test_sum(self):
        assert 10 == calculator.sum(5,5)
       
    def test_minus(self):
        assert 0 == calculator.minus(5,5)
