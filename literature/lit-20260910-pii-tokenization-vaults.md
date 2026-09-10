---
id: lit-20260910-pii-tokenization-vaults
title: "PII tokenization vaults (Skyflow, VGS) vs bank aggregators"
type: literature
status: active
created: 2026-09-10
updated: 2026-09-10
sources: ["https://www.skyflow.com/product/data-privacy-vault", "https://www.verygoodsecurity.com/products/vault", "https://plaid.com"]
harnesses: [hermes, omp]
domains: [cs, frameworks, tool-use]
confidence: high
tags: [literature, pii, vault, tokenize]
---

# PII tokenization vaults

## Claim (one sentence)

SSN / account numbers over HTTP are a privacy vault + outbound connection; bank login is Plaid-class OAuth, not Playwright.

## Evidence

- Skyflow / VGS / Basis Theory: collect UI. Agent holds `tok_…`. Outbound route detokenizes into an allowlisted partner HTTPS request only.
- Plaid / Finicity / MX: bank connection as OAuth-shaped token. Hermes #12324 (Teknium, finance+health sync) already names Plaid. Do not compete; constrain so the agent never sees raw account numbers when a partner API exists.
- File PDFs: vendors can file-token on their HTTP connections. IRS HTML forms are a tax API or a human.

## Fact vs interpretation

Fact: Hermes vault kinds are only login / payment / address. Redaction is exact substring on text.
Interpretation: stuffing SSN into an address field is not noninterference. Documents are a different product than identity fields.

## Links

- [[permanent/perm-20260910-hermes-vault-is-login-payment-address]]
- [[permanent/perm-20260910-identity-fields-are-not-documents]]
- [[permanent/perm-20260910-screenshots-bypass-vault-redaction]]
