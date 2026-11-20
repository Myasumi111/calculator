Q. why did 0.1 + 0.2 == 0.3 fail, and what does pytest.approx do instead? 
A. Unless you specify the tolerance, Python calculates 0.1 + 0.2 = 0.30000000000000004 which doesn't match 0.3 but pytest.approx() passes the result if it's close enough like 0.3 as long as it is within the tolerance range.

Q. And why did add turn back into a stub when you switched to feature/subtract?
A. add() didn't turn back into a stub. add() was never changed in feature/subtract.