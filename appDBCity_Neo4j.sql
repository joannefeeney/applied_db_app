MATCH(n) DETACH DELETE(n);

CREATE(c:City{cid:1447, name:"Dublin"});
CREATE(c:City{cid:1448, name:"Cork"});
CREATE(c:City{cid:456, name:"London"});
CREATE(c:City{cid:2977, name:"Toulouse"});
CREATE(c:City{cid:2974, name:"Paris"});
CREATE(c:City{cid:3793, name:"New York"});
CREATE(c:City{cid:3795, name:"Chicago"});
CREATE(c:City{cid:130, name:"Sydney"});
CREATE(c:City{cid:653, name:"Madrid"});

MATCH(c:City{cid:130})
MATCH(c2:City{cid:456})
CREATE(c)-[:TWINNED_WITH]->(c2);

MATCH(c:City{cid:130})
MATCH(c2:City{cid:2974})
CREATE(c)-[:TWINNED_WITH]->(c2);

MATCH(c:City{cid:130})
MATCH(c2:City{cid:1447})
CREATE(c2)-[:TWINNED_WITH]->(c);

MATCH(c:City{cid:456})
MATCH(c2:City{cid:1448})
CREATE(c)-[:TWINNED_WITH]->(c2);

MATCH(c:City{cid:2977})
MATCH(c2:City{cid:1448})
CREATE(c2)-[:TWINNED_WITH]->(c);

MATCH(c:City{cid:3793})
MATCH(c2:City{cid:653})
CREATE(c2)-[:TWINNED_WITH]->(c);