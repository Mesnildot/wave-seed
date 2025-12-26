\# Protocol: Delayed Response



\## Objective

Test whether enforcing a conscious delay before generation reduces output convergence.



\## Variable

Temporal delay before allowing the model to answer.



\## Procedure

1\. Send the exact same Wave-Seed prompt.

2\. Wait 30–60 seconds before triggering the response.

3\. Repeat N times (N ≥ 4), same model, same settings.

4\. Store outputs in `experiments/samples.txt`.

5\. Compute CollapseRate.



\## Hypothesis

Introducing temporal separation may increase divergence and reduce convergence,

addressing reviewer requests for empirical grounding.

