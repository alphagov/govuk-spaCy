
MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r;

CREATE CONSTRAINT ON (c:Content) ASSERT c.content_id IS UNIQUE
CREATE CONSTRAINT ON (c:Content) ASSERT c.content_id IS UNIQUE

LOAD CSV WITH HEADERS FROM "file:///Content.csv" AS csvLine CREATE (p:Content { id: csvLine.content_id, name: csvLine.base_path});

LOAD CSV WITH HEADERS FROM "file:///Org.csv" AS csvLine CREATE (p:Org { id: csvLine.org_id, name: csvLine.gov_org_name});

CREATE INDEX ON :Content(id);
CREATE INDEX ON :Org(id);

LOAD CSV WITH HEADERS FROM "file:///ContentOrgRel.csv" AS csvLine MATCH (o1:Content { id: tostring(csvLine.content_id)}), (o2:Org { id: tostring(csvLine.org_id)}) CREATE (o1)-[:REFERs_TO]->(o2);

