# Minimal harness example

Consider one durable agent loop that resolves support cases with tools and a human owner. At this system boundary the loop may be the single S1 operation. Scheduling and retry rules provide limited coordination over its internal activities; budget and stop controls contribute to S3; sampled human review of raw cases may contribute to S3* when it can challenge the loop's own success claims.

External policy changes and changing customer needs require an S4 function, perhaps performed periodically by a product team. The owner and organizational governance retain S5 authority. These functions need not be separate agents.

The example is minimal because it has one principal S1 unit. It should not be expanded into six agents merely to mirror the labels. If the operation later divides into independently accountable case-handling units, stronger S2 and S3 relationships may become necessary.
