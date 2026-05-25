---
tags: ["2.8"]
itaa-lex-sectie: ""
wet: "Explanatory Statement to the Multilateral Convention to Implement Tax Treaty Related Measures to Prevent BEPS"
bron_rol: "interpretatief"
status: "beschikbaar"
bijgewerkt: "24.11.2016"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/MLI-Explanatory-Statement-2016.pdf
      sha256: 2ec61cfa2cc77e9f952a2ddce059d44ad43bc5e709eabb1a8853e26c8a6b2c9d
      version: 24.11.2016
      pages:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 0c77206e
    model:
    prompt_version:
  generated_at: '2026-05-19T15:03:26Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-19T15:31:14Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Inhoud volledig aanwezig: alle 359 genummerde alinea's en de bijlage met Action Reports zijn zichtbaar. Heading-count is minimaal (2 ##-headings voor ca. 284 000 chars) maar de chunker splitst automatisch op alinea-grenzen. Het enige categorieprobleem zijn bullet-symbolen (•) in de inleidende opsomming (ca. 5 regels) — dit zijn source-typos uit de originele PDF, niet ETL-artefacten. Geen form-feeds, geen scrambled woorden in de lopende tekst."
    caveat:
    layer1:
      status: warn
      run_id: 20260519-150326
      run_at: '2026-05-19T15:03:27Z'
      heading_count: 2
      max_section_chars: 284323
      file_size_chars: 287053
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ##-niveau: 284323 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-19T15:31:14Z'
      rationale: "Inhoud volledig aanwezig: alle 359 genummerde alinea's en de bijlage met Action Reports zijn zichtbaar. Heading-count is minimaal (2 ##-headings voor ca. 284 000 chars) maar de chunker splitst automatisch op alinea-grenzen. Het enige categorieprobleem zijn bullet-symbolen (•) in de inleidende opsomming (ca. 5 regels) — dit zijn source-typos uit de originele PDF, niet ETL-artefacten. Geen form-feeds, geen scrambled woorden in de lopende tekst."
      concrete_problemen:
        - regel: 88
          categorie: C
          type: source-typo — bullet-symbool • in plaats van - of *
          voorbeeld: •  Specifying the tax treaties to which the Convention applies... (5 bullets totaal)
        - regel: 52
          categorie: B
          type: structuur — één massasectie van 284 000 chars
          voorbeeld: 'Gehele verklarende tekst valt onder één ##-heading; chunker compenseert'
---

# MLI Explanatory Statement

*Bijgewerkt tot en met 24.11.2016 — gecoördineerde versie.*

## EXPLANATORY STATEMENT TO THE MULTILATERAL CONVENTION TO IMPLEMENT TAX TREATY RELATED MEASURES TO PREVENT BASE EROSION AND PROFIT SHIFTING

Background

1.  The Multilateral Convention to Implement Tax Treaty Related Measures to Prevent Base Erosion  and Profit Shifting (the Convention) is one of the outcomes of the OECD/G20 Project to tackle Base  Erosion and Profit Shifting (the “BEPS Project”) i.e. tax planning strategies that exploit gaps and  mismatches in tax rules to artificially shift profits to low or no-tax locations where there is little or no  economic activity, resulting in little or no overall corporate tax being paid.

2.  The BEPS Action Plan was developed by the OECD Committee on Fiscal Affairs (CFA) and  endorsed by the G20 Leaders in September 2013 . It identified 15 actions to address base erosion and profit  shifting (BEPS) in a comprehensive manner, and set out deadlines to implement those actions. Action 15  of the BEPS Action Plan provided for an analysis of the possible development of a multilateral instrument  to implement tax treaty related BEPS measures “to enable jurisdictions that wish to do so to implement  measures developed in the course of the work on BEPS and amend bilateral tax treaties”.

3.  After two years of work, the CFA, including all OECD and G20 countries working on an equal  footing, produced the Final BEPS Package, which was endorsed by the OECD Council and the G20  Leaders in November 2015. The Final BEPS Package, in the form of reports on each of the 15 actions  accompanied by an Explanatory Statement, gives countries and economies the tools they need to ensure  that profits are taxed where economic activities generating the profits are performed and where value is  created, while at the same time giving businesses greater certainty by reducing disputes over the  application of international tax rules and standardising compliance requirements. It was agreed that a  number of the BEPS measures are minimum standards, meaning that countries have agreed that the  standard must be implemented.

4.  Implementation of the Final BEPS Package will require changes to model tax conventions, as  well as to the bilateral tax treaties based on those model conventions. The sheer number of bilateral treaties  (more than 3000) would make bilateral updates to the treaty network burdensome and time-consuming,  limiting the effectiveness of multilateral efforts.

5.  The Action 15 Report, “Developing a Multilateral Instrument to Modify Bilateral Tax Treaties”,  concluded that a multilateral instrument, providing an innovative approach to enable countries to swiftly  modify their bilateral tax treaties to implement measures developed in the course of the work on BEPS, is  desirable and feasible, and that negotiations for such an instrument should be convened quickly. The  Action 15 Report was developed with the assistance of a group of experts in public international law and  international tax law.

6.  In line with the Action 15 Report, a mandate for the formation of an ad hoc Group for the  development of a multilateral instrument was approved by the CFA and endorsed by the G20 Finance  Ministers and Central Bank Governors in February 2015. The mandate provided that the ad hoc Group  should develop a multilateral instrument to modify existing bilateral tax treaties in order to swiftly

implement the tax treaty measures developed in the course of the OECD/G20 BEPS Project. It also  provided that the ad hoc Group should conclude its work and open the multilateral instrument for signature  by 31 December 2016.

7.  The ad hoc Group was open to all interested countries participating on an equal footing. 99  countries participated in the ad hoc Group as members. Four non-State jurisdictions and seven  international or regional organisations participated as observers. The Chair of the ad hoc Group was Mr.  Mike Williams of the United Kingdom.

8.  The substance of the tax treaty-related BEPS measures (under BEPS Actions 2, 6, 7 and 14) was  agreed as part of the Final BEPS Package. Accordingly, the negotiation in the ad hoc Group was focused  on how the Convention would need to modify the provisions of bilateral or regional tax agreements in  order to implement those measures.

9.  The Action 14 Report, “Making Dispute Resolution Mechanisms More Effective”, also provided  that a mandatory binding mutual agreement procedure arbitration provision would be developed as part of  the negotiation of the Convention. Accordingly, the ad hoc Group established a Sub-Group on Arbitration  for this purpose in which 27 countries participated as members. The Sub-Group was chaired by Ms. Ingela  Willfors of Sweden. Unlike the other BEPS measures, negotiation of the mandatory binding arbitration  provision related both to developing the substance of the provision and to the modalities of its  implementation in bilateral or regional tax agreements.

10.  Over the course of the negotiations, the ad hoc Group met six times and the Sub-Group on  Arbitration met five times.

11.  The text of this explanatory statement to accompany the Convention (“Explanatory Statement”)  was prepared by the participants in the ad hoc Group, and in the Sub-Group on Arbitration, to provide  clarification of the approach taken in the Convention and how each provision is intended to affect tax  agreements covered by the Convention (“Covered Tax Agreements”). It therefore reflects the agreed  understanding of the negotiators with respect to the Convention. It includes descriptions of the types of  treaty provisions which are intended to be covered and the ways in which they are intended to be modified.  The members of the ad hoc group adopted this Explanatory Statement on 24 November 2016 at the same  time as adopting the text of the Convention.

12.  The development of the BEPS measures that are implemented by the Convention also included  development of commentary which was intended to be used in the interpretation of those provisions. While  this Explanatory Statement is intended to clarify the operation of the Convention to modify Covered Tax  Agreements, it is not intended to address the interpretation of the underlying BEPS measures (except with  respect to the mandatory binding arbitration provision contained in Articles 18 through 26, as noted below  in paragraphs 19 and 20). Accordingly, the provisions contained in Articles 3 through 17 should be  interpreted in accordance with the ordinary principle of treaty interpretation, which is that a treaty shall be  interpreted in good faith in accordance with the ordinary meaning to be given to the terms of the treaty in  their context and in light of its object and purpose. In this regard, the object and purpose of the Convention  is to implement the tax treaty-related BEPS measures. The commentary that was developed during the  course of the BEPS Project and reflected in the Final BEPS Package has particular relevance in this regard.  It should be noted that while in some cases, as noted below, the provisions of the Convention differ in form  from the model provisions that were produced through the BEPS Project, unless noted otherwise, these  modifications are not intended to make substantive changes to those provisions. Instead, they are intended  to implement the agreed BEPS measures in the context of a multilateral instrument that applies to a widely  varied network of existing treaties.

Approach taken in the Convention

13.  The Convention operates to modify tax treaties between two or more Parties to the Convention. It  will not function in the same way as an amending protocol to a single existing treaty, which would directly  amend the text of the Covered Tax Agreement; instead, it will be applied alongside existing tax treaties,  modifying their application in order to implement the BEPS measures. As a result, while for internal  purposes, some Parties may develop consolidated versions of their Covered Tax Agreements as modified  by the Convention, doing so is not a prerequisite for the application of the Convention. As noted below, it  is possible for Contracting Jurisdictions to agree subsequently to different modifications to their Covered  Tax Agreement than those foreseen in the Convention.

14.  As noted above, the purpose of the Convention is to swiftly implement the tax treaty-related  BEPS measures. Consistent with that purpose, the ad hoc Group considered that the Convention should  enable all Parties to meet the treaty-related minimum standards that were agreed as part of the Final BEPS  package, which are the minimum standard for the prevention of treaty abuse under Action 6 and the  minimum standard for the improvement of dispute resolution under Action 14. Given, however, that each  of those minimum standards can be satisfied in multiple different ways, and given the broad range of  countries and jurisdictions involved in developing the Convention, the Convention needed to be flexible  enough to accommodate the positions of different countries and jurisdictions while remaining consistent  with its purpose. The Convention also needed to provide flexibility in relation to provisions that did not  reflect minimum standards, particularly in relation to how such provisions interact with provisions in  Covered Tax Agreements. The Convention provides that flexibility in the following ways:

•  Specifying the tax treaties to which the Convention applies (the “Covered Tax  Agreements”). Although it is intended that the Convention would apply to the maximum  possible number of existing agreements, there may be circumstances in which a Party prefers not  to include a specific agreement in the scope of application of the Convention because, for  example, the agreement has been recently renegotiated to implement the outcomes of the BEPS  Project, or is currently under renegotiation with the intent of implementing those outcomes in the  renegotiated agreement. This is accomplished by ensuring that the Convention will apply only to  an agreement specifically listed by the parties (referred to throughout the Convention as  “Contracting Jurisdictions”) to that agreement.

•  Flexibility with respect to provisions that relate to a minimum standard. Where a provision  reflects a BEPS minimum standard, opting out of that provision is possible only in limited  circumstances, such as where a Party’s Covered Tax Agreements already meet that minimum  standard. Where a minimum standard can be satisfied in multiple alternative ways, the  Convention does not give preference to a particular way of meeting the minimum standard. To  ensure that the minimum standard can be met in such circumstances, however, in cases where  Contracting Jurisdictions each adopt a different approach to meeting a minimum standard that  requires the inclusion of a specific type of treaty provision, those Contracting Jurisdictions must  endeavour to reach a mutually satisfactory solution consistent with the minimum standard. It  should be noted that whether a Covered Tax Agreement (as it may be amended through bilateral  negotiations) meets the minimum standard would be determined in the course of the overall  review and monitoring process by the Inclusive Framework on BEPS, which brings together a  large number of countries and jurisdictions to work on the implementation of the Final BEPS  Package.

•  Opting out of provisions or parts of provisions with respect to all Covered Tax Agreements.  Where a substantive provision does not reflect a minimum standard, a Party is generally given the  flexibility to opt out of that provision entirely (or, in some cases, out of part of that provision).

This is accomplished through the mechanism of reservations, which are specifically defined for  each substantive Article of the Convention. Where a Party uses a reservation to opt out of a  provision of the Convention, that provision will not apply as between the reserving Party and all  other Parties to the Convention. Accordingly, the modification foreseen by that provision will not  be made to any of the Covered Tax Agreements of the reserving Party.

•  Opting out of provisions or parts of provisions with respect to Covered Tax Agreements  that contain existing provisions with specific, objectively defined characteristics. The ad hoc  Group recognised that even where a Party intends to apply a particular provision of the  Convention to its treaty network, it may have policy reasons for preserving the application of  specific types of existing provisions. To accommodate this, in a number of cases the Convention  permits a Party to reserve the right to opt out of applying a provision to a subset of Covered Tax  Agreements in order to preserve existing provisions that have specific, objectively defined  characteristics. Except as otherwise provided, such reservations are not mutually exclusive. As a  result, where a Party makes one or more such reservations, all such reservations will apply as  between the reserving Party and all Contracting Jurisdictions to the Covered Tax Agreements that  are covered by such reservations.

•  Choosing to apply optional provisions and alternative provisions. In some cases, the output of  the work on BEPS produced multiple alternative ways to address a particular BEPS issue. In  other cases, the work resulted in a main provision that could be supplemented with an additional  provision. The Convention incorporates a number of alternatives or optional provisions that  generally will apply only if all Contracting Jurisdictions to a Covered Tax Agreement  affirmatively choose to apply them.

15.  The structure of each substantive provision of the Convention (with the exception of the  provisions of Part VI) is as follows:

•  Agreed BEPS measure that forms the basis of the provision of the Convention. In general,  each of Articles 3 through 17 begins with one or more paragraphs reflecting one of the BEPS  measures. These paragraphs generally duplicate the language of the provisions of the OECD  Model Tax Convention that were developed during the course of the BEPS Project, with a  number of types of modifications, including:

o  Changes in terminology to conform the model provision to the terminology used in  the Convention. For example, to appropriately reflect the scope of the Convention, as  well as the fact that individual tax treaties may have a variety of titles, the term  “Covered Tax Agreement” is used in place of the term “Convention” in the OECD  Model Tax Convention and the United Nations Model Double Taxation Convention  between Developed and Developing Countries (“UN Model Tax Convention”). In  addition, “Contracting Jurisdiction” is used in place of “Contracting State” to refer to  the parties to a Covered Tax Agreement, to reflect the fact that the Convention may  modify agreements in relation to which one or more party is a non-State jurisdiction.

o  Replacement of cross-references to specific Articles and paragraphs with  descriptions of those provisions. A number of the BEPS measures interact with  existing provisions of tax agreements that were not modified. Because existing tax  agreements vary significantly from each other, it was not possible for the provisions of  the Convention to identify those provisions by referring to specific articles and  paragraph numbers. Instead, where a reference to the provisions of existing tax

agreements is necessary, the Convention uses descriptive language to identify those  provisions.

o  Modifications to reflect differences in underlying provisions. In some cases, the  BEPS Project provided solutions to issues arising under specific provisions of the  OECD Model Tax Convention. The model provisions required modification in the  context of the Convention to ensure that they could apply appropriately in the context  of agreements that do depart from the OECD Model Tax Convention. For example, the  work on Action 6 produced modifications to Article 10(2) of the OECD Model Tax  Convention to require that a minimum holding period be satisfied in order for a  company to be entitled to a reduced rate on dividends from a subsidiary. This provision  was based on the dividend withholding rates and ownership thresholds contained in the  OECD Model Tax Convention, and needed to be modified in order to reflect the wide  variety of similar provisions in existing agreements.

•  Compatibility clause(s) which define the relationship between the provisions of the  Convention and Covered Tax Agreements in objective terms. As noted above, many of the  provisions of the Convention overlap with provisions found in Covered Tax Agreements. In some  cases, they can be applied without conflict with the provisions of Covered Tax Agreements.  Where the provisions of the Convention may conflict with existing provisions covering the same  subject matter, however, this conflict is addressed through one or more compatibility clauses  which may, for example, describe the existing provisions which the Convention is intended to  supersede, as well as the effect on Covered Tax Agreements that do not contain a provision of the  same type.

•  Reservation clause(s) that define the reservation(s) permitted with respect to each provision  (in line with the agreement reached on the relevant BEPS measure). In many cases, Parties  are permitted to opt out of applying particular provisions to their Covered Tax Agreements, either  across the board, or with respect to a subset of Covered Tax Agreements based on objective  criteria (see paragraph 14 above). This is accomplished through one or more paragraphs in each  Article that set out a closed list of permitted reservations. To ensure clarity, a Party making a  reservation that applies to a subset of Covered Tax Agreements based on objective criteria is  required to provide a list of the existing provisions in their Covered Tax Agreements that fall  within the defined scope of that reservation. As noted above, where a Party has made a  reservation with respect to a provision, that reservation will apply as between that Party and all  other Parties to the Convention.

•  Notification clause(s) reflecting choices of optional provisions. Each Article that permits a  Party to choose among alternative provisions requires each Party making such a choice to notify  the Depositary of its choice, and describes the consequences of a mismatch between the  Contracting Jurisdictions to a Covered Tax Agreement, which vary depending on the provision in  question.

•  Notification clause(s) to ensure clarity about existing provisions that are within the scope of  compatibility clauses. To ensure clarity and transparency about the application of the  Convention, where a provision supersedes or modifies specific types of existing provisions of a  Covered Tax Agreement, Parties are generally required to make a notification specifying which  Covered Tax Agreements contain provisions of that type. It is expected that Parties would use  their best efforts to identify all provisions that are within the objective scope of the compatibility  clause. It is therefore not intended that Parties would choose to omit some relevant provisions

while listing others. The effect of these notifications varies depending on the type of  compatibility clause that applies to that provision, as follows:

o Provision of the Convention applies “in place of” an existing provision of a Covered  Tax Agreement. Where a provision of the Convention applies only “in place of” an  existing provision, the provision is intended to replace an existing provision if one exists,  and is not intended to apply if an existing provision does not exist. In such cases, the  notification provision states that the provision of the Convention will apply only in cases  where all Contracting Jurisdictions make a notification with respect to the existing  provision of the Covered Tax Agreement as described in the Convention.

o Provision of the Convention “applies to” or “modifies” an existing provision of a  Covered Tax Agreement. Where a provision of the Convention “applies to” or  “modifies” an existing provision, the provision of the Convention is intended to change  the application of an existing provision without replacing it, and therefore can only  apply if there is an existing provision. In such cases, the notification provision states that  the provision of the Convention will apply only in cases where all Contracting  Jurisdictions make a notification with respect to the existing provision of the Covered  Tax Agreement.

o Provision of the Convention applies “in the absence of” an existing provision of a  Covered Tax Agreement. Where a provision of the Convention applies only “in the  absence of” an existing provision, the provision of the Convention will apply only in  cases where all Contracting Jurisdictions notify the absence of an existing provision of  the Covered Tax Agreement.

o Provision of the Convention applies “in place of or in the absence of” an existing  provision of a Covered Tax Agreement. Where a provision of the Convention applies  “in place of or in the absence of” an existing provision, the provision of the Convention  will apply in all cases. If all Contracting Jurisdictions notify the existence of an existing  provision, that provision will be replaced by the provision of the Convention (to the  extent described in the relevant compatibility clause). Where the Contracting  Jurisdictions do not notify the existence of a provision, the provision of the Convention  will still apply. If there is in fact a relevant existing provision which has not been  notified by all Contracting Jurisdictions, the provision of the Convention will prevail  over that existing provision, superseding it to the extent that it is incompatible with the  relevant provision of the Convention. If there is no existing provision, the provision of  the Convention will, in effect, be added to the Covered Tax Agreement.

16.   The approach described in the last bullet of the previous paragraph is intended to reflect the  ordinary rule of treaty interpretation, as reflected in Article 30(3) of the Vienna Convention on the Law of  Treaties, under which an earlier treaty between parties that are also parties to a later treaty will apply only  to the extent that its provisions are compatible with those of the later treaty.

17.  An existing provision of a Covered Tax Agreement is considered “incompatible” with a  provision of the Convention if there is a conflict between the two provisions. For example, Article 17(2) of  the Convention provides that Article 17(1) will apply in place of or in the absence of existing provisions  that “require a Contracting Jurisdiction to make an appropriate adjustment to the amount of the tax charged  therein on the profits of an enterprise of that Contracting Jurisdiction where the other Contracting  Jurisdiction includes those profits in the profits of an enterprise of that other Contracting Jurisdiction and  taxes those profits accordingly, and the profits so included are profits which would have accrued to the

enterprise of that other Contracting Jurisdiction if the conditions made between the two enterprises had  been those which would have been made between independent enterprises." Certain existing provisions,  however, provide only that a Contracting Jurisdiction may make a corresponding adjustment or may  consult for that purpose, but do not require corresponding adjustments to be made in any particular  circumstances. Those existing provisions would be outside the scope of paragraph Article 17(2), meaning  that they would therefore continue to apply unless they are incompatible. To the extent that such provisions  would permit a Contracting Jurisdiction to choose not to make an appropriate adjustment even in the  situation in which the adjustment made by the other Contracting Jurisdiction was justified, however, such  provisions would be incompatible with 17(1). As a result, Article 17(1) would supersede such provisions,  meaning that its application would replace the application of such provisions to the extent necessary to  avoid the conflict between the provisions.

18.  As noted above, it is expected that Parties would use their best efforts to identify all provisions  that are within the objective scope of each compatibility clause. This should reduce to a minimum  situations in which a relevant existing provision is not identified by the Contracting Jurisdictions to a  Covered Tax Agreement. Such situations are not impossible, however, either because the Contracting  Jurisdictions to a Covered Tax Agreement disagree about whether a particular provision is within the scope  of a compatibility clause; or because both Contracting Jurisdictions agree that there is a relevant provision,  but disagree about which provision it is. To minimise these possibilities, lists of notifications albeit  provisional are required to be provided at the time of signature, so that Signatories will have the  opportunity to discuss any mismatches in notification and correct them prior to finalisation of those lists.  To the extent that such situations nevertheless arise, any disagreement between the Contracting  Jurisdictions as to whether existing provisions are within the scope of a compatibility clause could be  settled through the mutual agreement procedure provided for in the Covered Tax Agreement or, if  necessary, through a Conference of the Parties convened in accordance with the procedure set out in

Approach taken in Developing the Optional Provision on Mandatory Binding Arbitration of Mutual  Agreement Procedure Cases

19.  Part VI of the Convention (Articles 18 through 26) reflects the result of the work of the Sub- Group on Arbitration to develop provisions for the mandatory binding arbitration of mutual agreement  procedure cases in which the competent authorities are unable to reach agreement within a fixed period of  time. As noted above, unlike the other BEPS measures, this work includes the development of the  substantive content of a mandatory binding arbitration provision. As a result, unlike Articles 3 through 17,  the provisions of this Explanatory Statement related to Part VI address both the substance of those  provisions and its technical application to Covered Tax Agreements.

20.  Unlike the other Articles of the Convention, Part VI applies only between Parties that expressly  choose to apply Part VI with respect to their Covered Tax Agreements. The structure of the Articles of Part  VI also differs from the structure of the other Articles of the Convention. These differences reflect the fact  that Part VI is intended to operate as a single cohesive arbitration provision. Thus, as discussed in more  detail below, rather than including a compatibility clause in each Article of Part VI, rules for compatibility  with existing provisions are consolidated in Article 26. In addition, while Part VI includes some defined  reservations, Parties that choose to apply Part VI are also permitted to formulate their own reservations  with respect to the scope of cases that will be eligible for arbitration (subject to acceptance by the other  Parties), as discussed in the sections of this Explanatory Statement related to Article 28(2).

Preamble

21.  The preamble describes the overall purpose of the Convention to implement tax treaty-related  measures produced as part of the Final BEPS Package in a swift, co-ordinated and consistent manner  across the network of existing tax treaties without the need to bilaterally renegotiate each such treaty.

22.  The penultimate paragraph of the preamble notes that the Parties recognise the need to ensure  that existing agreements for the avoidance of double taxation on income are interpreted to eliminate double  taxation with respect to the taxes covered by those agreements without creating opportunities for non- taxation or reduced taxation through tax evasion or avoidance (including through treaty-shopping  arrangements aimed at obtaining reliefs provided in those agreements for the indirect benefit of residents of  third jurisdictions). This statement relates in particular to Article 6(1), which aims to modify the preambles  of Covered Tax Agreements to include the following text:

Intending to eliminate double taxation with respect to the taxes covered by this agreement  without creating opportunities for non-taxation or reduced taxation through tax evasion or  avoidance (including through treaty-shopping arrangements aimed at obtaining reliefs  provided in this agreement for the indirect benefit of residents of third jurisdictions),

23.  The inclusion of this statement in the preamble to the Convention is intended to clarify the intent  of the Parties to ensure that Covered Tax Agreements be interpreted in line with the preamble language  foreseen in Article 6(1).

Part I. Scope and Interpretation of Terms

Article 1 - Scope of the Convention

24.

Article 2 – Interpretation of Terms

Paragraph 1

Covered Tax Agreement

25.  Paragraph 1(a) defines “Covered Tax Agreement”, the term used for the agreements that will be  modified by the Convention. This will include agreements for the avoidance of double taxation with  respect to taxes on income that are in force between two or more Parties to the Convention, or as noted  below, jurisdictions for whose international relations a Party is responsible. This would include agreements  that cover capital taxes, or taxes on capital gains, in addition to income taxes. The Convention is not,  however, intended to apply to agreements applying solely to shipping and air transport or social security.

26.  To avoid confusion or uncertainty about the scope of agreements covered, the Convention  modifies only an agreement that has been specifically identified in a notification to the Depositary by each  Party to the Convention that is either a Contracting Jurisdiction to that agreement or responsible for the  international relations of a party to the agreement. This notification would identify the agreement along  with any instruments that have amended the agreement, along with any accompanying instruments that  modify the application of the agreement. This approach provides for flexibility as to which existing  agreements are covered by the Convention. Although it is intended that the Convention would apply to the  maximum possible number of existing agreements, there may be circumstances in which a Party prefers  not to include a specific agreement in the scope of application of the Convention. For example, a Party  may wish not to include an agreement in the scope of application of the Convention based on the fact that  the agreement has been recently renegotiated to implement the outcomes of the BEPS Project, or is  currently under renegotiation with the intent of implementing those outcomes in the renegotiated  agreement.

27.  Paragraph 1(a)(i)(B) enables a State that is a Party to the Convention to include in its list of  Covered Tax Agreements tax agreements which have been entered into by a jurisdiction or territory for  whose international relations the State Party is responsible. This is intended to cover the situation of  jurisdictions or territories which, under the arrangements with the State responsible for their international  relations, have the ability to conclude tax agreements in their own right.

28.  Accordingly, there are two ways in which the Convention may cover tax agreements concluded  by non-State jurisdictions or territories: (i) jurisdictions may become Parties to the Convention by being  listed by name in the text of Article 27(1)(b) at the time of adoption of the text of the Convention or by  being subsequently authorised to sign and ratify the Convention by a decision by consensus of the Parties  and Signatories pursuant to Article 27(1)(c) (see paragraphs 261 and 262 of the Explanatory Statement  below); or (ii) pursuant to Article 2(1)(a)(i)(B), a State Party may include in its list of Covered Tax  Agreements, tax agreements concluded by a jurisdiction or territory for whose international relations it is  responsible.

29.  In cases where a State Party avails itself of paragraph 1(a)(i)(B), it shall make reservations and  notifications in respect of the jurisdiction or territory in question, which will apply to all Covered Tax  Agreements of that jurisdiction or territory. These reservations and notifications can be different from  those of the State Party itself, as described in Articles 28(4) and 29(2) of the Convention.

30.  The Convention may also cover tax agreements entered into by a State Party “on behalf” of a  non-State jurisdiction or territory for whose international relations it is responsible. In such cases, the State  Party would include those tax agreements in its list of tax agreements under paragraph 1(a)(i)(A) but has  the possibility under Articles 28(4) and 29(2) to make reservations and notifications in respect of that  jurisdiction or territory which may differ from the State Party’s own list of reservations and notifications.

31.  It is important to note that the geographical scope of a Covered Tax Agreement remains as  defined in that Covered Tax Agreement and is unchanged by the Convention. Accordingly, the provisions  of Covered Tax Agreements which are modified by the Convention will apply with the same geographic  scope as the original Covered Tax Agreement.

32.  It is possible for a Party to include in the list of agreements provided under paragraph 1(a)(ii) an  agreement which has been signed but has not yet entered into force. In such cases, the Party should notify  the Depositary in due course of the date of entry into force of that agreement since that is the date on which  it can become a Covered Tax Agreement. Where such date is after the entry into force of the Convention  with respect to such Party pursuant to Article 34(2), such a notification will be considered an extension of  the list of agreements pursuant to Article 29(5).

33.  In providing its list of agreements under paragraph 1(a)(ii), a Party should include not only a  reference to the original agreement but also to any accompanying instruments that modify the application  of the agreement, as well as any instruments which have subsequently amended the agreement. This  ensures clarity about the content of the agreement in force at the time when it is modified by the  Convention. However, it is important to note that the Convention is not intended to freeze in time the  underlying agreement and that Contracting Jurisdictions may of course decide to further amend the  underlying agreement after it has been modified by the Convention. The right of the Contracting  Jurisdictions to further amend their Covered Tax Agreements is intended to remain unaffected, irrespective  of whether the further modifications relate to provisions that have been modified by the application of the  Convention. This is reflected in Article 30 of the Convention, which provides that subsequent  modifications to Covered Tax Agreements may be agreed between the Contracting Jurisdictions.

Party

34.  The term “Party” is used throughout the Convention to refer to States, as well as jurisdictions  which have signed the Convention pursuant to Article 27(1)(b) or (c), for which the Convention is in force  pursuant to Article 34.

Contracting Jurisdiction

35.  The term “Contracting Jurisdiction” refers to the States, jurisdictions or territories that are parties  to a Covered Tax Agreement. It is used instead of the more commonly used terms “Contracting State”  (which is inaccurate due to the potential application of the Convention to tax agreements to which a non- State jurisdiction is a party) and “Contracting Party”, which could cause confusion given that “Party”  refers to a party to the Convention.

Signatory

36.  The term “Signatory”, which is used exclusively in the final provisions of the Convention, refers  to States and jurisdictions that have signed the Convention pursuant to Article 27(1) but for which the  Convention is not yet in force.

Paragraph 2

37.  This paragraph provides a general rule of interpretation for terms used in the Convention but not  defined therein. Any term not defined in the Convention shall, unless the context otherwise requires, have  the meaning that it has under the relevant Covered Tax Agreement at the time the Convention is being  applied.

38.  With respect to a term not explicitly defined in the Convention or in the relevant Covered Tax  Agreement, Covered Tax Agreements generally provide that any term not defined shall, unless the context  otherwise requires, have the meaning it has at the time the Covered Tax Agreement is being applied under  the domestic law of the Contracting Jurisdiction applying the Covered Tax Agreement, the meaning given  to that term under the tax laws of that Contracting Jurisdiction prevailing over a meaning given to the term  under other laws of that Contracting Jurisdiction. Where this rule is present in a Covered Tax Agreement, it  would apply for the purposes of determining the meaning of undefined terms in the Convention, unless the  context requires an alternative interpretation. For this purpose, the context would include the purpose of the  Convention, as described in paragraphs 1 through 14 above, and of the Covered Tax Agreement, as  reflected in the preamble as modified by Article 6 (see paragraphs 21 to 23 above, related to the preamble  of the Convention, and paragraph 76 below, related to Article 6).

Part II. Hybrid Mismatches

Article 3 – Transparent Entities

Paragraph 1

39.  The Action 2 Report, “Neutralising the Effects of Hybrid Mismatch Arrangements”, produced  new Article 1(2) of the OECD Model Tax Convention, which addresses income earned through transparent  entities. The text of that new Article 1(2), which is found in paragraph 435 (page 139) of the Action 2  Report, is as follows:

2. For the purposes of this Convention, income derived by or through an entity or  arrangement that is treated as wholly or partly fiscally transparent under the tax law of  either Contracting State shall be considered to be income of a resident of a Contracting  State but only to the extent that the income is treated, for purposes of taxation by that State,  as the income of a resident of that State.

40.

Paragraph 2

41.  Paragraph 2 implements changes related to the elimination of double taxation, as described in  paragraph 64 of the Action 6 Report “Preventing the Granting of Treaty Benefits in Inappropriate  Circumstances”, which were agreed as part of the follow-up work on Action 6. This provision is intended  to modify the application of the provisions related to methods for the elimination of double taxation, such  as those found in Articles 23A and 23B of the OECD and UN Model Tax Conventions.

Paragraph 3

42.  As discussed in further detail in paragraph 154 of the explanation related to Article 11(3),  paragraph 3 addresses the link between Article 3 and the saving clause in Article 11 by adding an  additional sentence to the end of paragraph 1. It will apply with respect to any Covered Tax Agreement for  which one or more Parties has reserved the right not to apply Article 11 pursuant to paragraph 3(a) of that  Article.

Paragraph 4

43.  A significant number of Covered Tax Agreements already include provisions addressing fiscally  transparent entities, and these provisions take a variety of forms. For example, while the provision  reflected in paragraph 1 is framed in terms when income is derived by a transparent entity, some provisions  are framed instead as definitions of the term “resident”. Other provisions contain more detailed rules  setting out particular circumstances under which income earned through an entity treated as transparent  under the laws of one of the Contracting Jurisdictions will be entitled to benefits.

44.  Paragraph 4 is the compatibility clause, which addresses the relationship between Article 3(1) (as  it may be modified by Article 3(3)) and existing provisions of the same type. It is intended to address all of  the above types of provision, by indicating that Article 3(1) (as it may be modified by Article 3(3)) would  replace provisions of a Covered Tax Agreement to the extent that they address whether income derived  through entities or arrangements that are treated as fiscally transparent under the tax law of a Contracting  Jurisdiction will be treated as income of a resident of a Contracting Jurisdiction, or would be added where  such provisions do not exist. Where an existing provision addresses both the treatment of fiscally

transparent entities and arrangements and the treatment of tax exempt entities that are not fiscally  transparent, such a provision would be superseded only with respect to the treatment of fiscally transparent  entities.

45.  Paragraph 1 will thus replace provisions addressing whether income derived through entities or  arrangements that are treated as fiscally transparent under the tax law of a Contracting Jurisdiction will be  treated as income of a resident of a Contracting Jurisdiction, whether such provisions are framed in terms  of a general rule along the lines of that found in the OECD Model Tax Convention, by identifying in detail  the treatment of specific fact patterns, or by describing the treatment of specific types of entities or  arrangements. It is not intended, however, that Article 3(1) (as it may be modified by paragraph 3) would  replace provisions that contain detailed “integrity rules” clarifying how an article of a Covered Tax  Agreement applies to a particular item of income derived by a resident of a Contracting Jurisdiction, such  as a rule deeming a beneficiary of a business trust to have a permanent establishment and attributing to that  permanent establishment the share of the business profits of the trust to which the beneficiary is  beneficially entitled. Although these latter types of integrity provision may apply to income that is derived  by or through an entity or arrangement that is treated as fiscally transparent under the tax law of a  Contracting Jurisdiction, they do not address whether that income will be treated as income of a resident of  a Contracting Jurisdiction for the purposes of Article 3(4). Rather, these latter provisions only operate  where the relevant item of income is already treated as income of a resident of a Contracting Jurisdiction  entitled to benefits under the relevant Covered Tax Agreement.

Paragraph 5

46.  A provision on fiscally transparent entities is not required in order to meet a minimum standard.  The reservation clauses in paragraph 5 therefore indicate that a Party may opt out of this Article entirely. In  addition, Parties may reserve the right to keep existing provisions addressing this issue; where either  Contracting Jurisdiction to a Covered Tax Agreement adopts such a reservation, the existing provision  would be preserved.

47.  It is also possible for a Party to reserve the right to retain existing provisions that would deny  benefits in the case of transparent entities established in third jurisdictions. Parties may also reserve the  right to retain existing provisions that provide more detail about the treatment of factual situations and  entities to which the provision is intended to apply (or to reserve the right to retain such provisions only  where they would deny benefits to transparent entities established in third jurisdictions). Parties may also  reserve the right for paragraph 2 not to apply to their Covered Tax Agreements. Finally, Parties may  reserve the right to replace such detailed provisions while leaving existing shorter provisions as they are.

Paragraph 6

48.  To ensure clarity about which existing provisions will be superseded by paragraph 1 (as it may be  modified by paragraph 3), paragraph 6 requires each Party (other than a Party that has reserved the right for  the entirety of Article 3 not to apply to all of its Covered Tax Agreements or for paragraph 1 not to apply  to its Covered Tax Agreements that already contain a provision described in paragraph 4) to notify the  Depositary of whether each of its Covered Tax Agreements contain an existing provision of the same type  that is not subject to a reservation under paragraph 5(c) through (e). Where a Party has made the  reservation described in paragraph 5(g), the notification would include only the provisions of the Covered  Tax Agreements that are subject to that reservation. Such a provision would be replaced by paragraph 1 (as  it may be modified by paragraph 3) to the extent provided in paragraph 4 where all parties to the Covered  Tax Agreement have made such a notification. In all other cases, paragraph 1 (as it may be modified by  paragraph 3) will apply to the Covered Tax Agreement, but the existing provisions of the Covered Tax

Agreement would be superseded only to the extent that those provisions are incompatible with paragraph 1  (as it may be modified by paragraph 3).

Article 4 – Dual Resident Entities

Paragraph 1

49.  Paragraph 1 modifies the rules for determining the treaty residence of a person other than an  individual that is a resident of more than one Contracting Jurisdiction, and is based on the text of Article  4(3) of the OECD Model Tax Convention produced in paragraph 48 (page 72) of the Action 6 Report,  which reads as follows:

3. Where by reason of the provisions of paragraph 1 a person other than an individual  is a resident of both Contracting States, the competent authorities of the Contracting States  shall endeavour to determine by mutual agreement the Contracting State of which such  person shall be deemed to be a resident for the purposes of the Convention, having regard to  its place of effective management, the place where it is incorporated or otherwise constituted  and any other relevant factors. In the absence of such agreement, such person shall not be  entitled to any relief or exemption from tax provided by this Convention except to the extent  and in such manner as may be agreed upon by the competent authorities of the Contracting  States.

50.  As with the other provisions of the Convention, Article 4(1) reflects changes to the model text to  conform the terminology used therein to the terminology used in the Convention and to replace cross  references to specific paragraphs with descriptions of those paragraphs.

Paragraph 2

51.  Paragraph 2 is the compatibility clause which describes the interaction between Article 4(1) and  provisions of Covered Tax Agreements. Recognising that within any given Covered Tax Agreement, it  would be important to have a single tie-breaker rule with respect to the residence of entities, paragraph 2  indicates that Article 4(1) (as it may be modified by the reservation under Article 4(3)(e)) would apply in  place of provisions of a Covered Tax Agreement that provide rules for determining whether a person other  than an individual shall be treated as a resident of one of the Contracting Jurisdictions in cases in which  that person would otherwise be treated as a resident of more than one Contracting Jurisdiction, or would be  added where such provisions do not exist.

52.  Existing “tie-breaker” provisions addressing the residence of persons other than individuals take  a variety of forms. For example, some (such as Article 4(3) of the UN Model Tax Convention, and of the  OECD Model Tax Convention prior to the BEPS Project) break the tie in favour of the place of effective  management, some focus on the place of organisation, and others call for determination by mutual  agreement but do not explicitly deny benefits in the absence of such a determination. Existing tie-breaker  provisions also include provisions addressing such cases by denying treaty benefits without requiring the  competent authorities to endeavour to reach mutual agreement on a single Contracting Jurisdiction of  residence. The provisions of Article 4 would replace all such types of tie-breaker rules with respect to the  residence of persons other than individuals. Where a single provision of a Covered Tax Agreement  provides for a tie-breaker rule applicable to both individuals and persons other than individuals, paragraph  1 would apply in place of that provision only to the extent that it relates to a person other than an individual.

53.

commonality of management, operations, shareholders’ rights, purpose and mission through an agreement  or a series of agreements between two parent companies, each with its own stock exchange listing, together  with special provisions in their respective articles of association including in some cases, for example, the  creation of special voting shares. Under these types of structures, while the participating companies retain  their separate entity legal status, the position of the parent company shareholders is, as far as possible, the  same as if they held shares in a single company, with the same dividend entitlement and same rights to  participate in the assets of the dual-listed companies in the event of a winding up. Arrangements of this  type occur in relatively few jurisdictions, and treaty provisions addressing them are typically customised in  detail to the circumstances of those jurisdictions in order to ensure the determination of a single  Contracting Jurisdiction of residence for each participating company.

Paragraph 3

54.  Given that provisions addressing cases in which a person other than an individual is a resident of  more than one Contracting Jurisdiction are not required in order to meet a minimum standard, paragraph  3(a) allows a Party to reserve the right not to apply the entirety of Article 4 to its Covered Tax Agreements,  and paragraph 3(b) through (d) allow a Party to opt out of applying the entirety of Article 4 to Covered Tax  Agreements that contain provisions with specific, objectively defined characteristics.

55.  Under paragraph 3(b), a Party may reserve the right for the entirety of Article 4 not to apply to  Covered Tax Agreements that already require the competent authorities of the Contracting Jurisdictions to  endeavour to reach agreement on a single Contracting Jurisdiction of residence. Paragraph 3(c), in contrast,  permits a Party to reserve the right for the entirety of Article 4 not to apply to its Covered Tax Agreements  that already deny treaty benefits without requiring the competent authorities of the Contracting  Jurisdictions to endeavour to reach mutual agreement on a single Contracting Jurisdiction of residence.  Paragraph 3(d) provides a more limited version of the reservation in paragraph 3(b), permitting a Party to  reserve the right for the entirety of Article 4 not to apply to Covered Tax Agreements that require  competent authorities of the Contracting Jurisdictions to endeavour to reach agreement on a single  Contracting Jurisdiction of residence for a person other than an individual and that set out the treatment of  that person where such an agreement cannot be reached.

56.  Under paragraph 3(e), a Party may also reserve the right to replace the last sentence of Article 4(1)  with the following text for the purposes of its Covered Tax Agreements: “In the absence of such agreement,  such person shall not be entitled to any relief or exemption from tax provided by the Covered Tax  Agreement.” In effect, this permits a Party to ensure that the competent authorities of the Contracting  Jurisdictions will not be permitted to agree to grant any relief or exemption from tax provided by the  Covered Tax Agreement unless they are able to agree on the Contracting Jurisdiction of which the person  described in paragraph shall be deemed to be a resident for the purposes of the Covered Tax Agreement.

57.  Recognising that the application of paragraph 3(e) may not be acceptable to all Parties, paragraph  3(f) permits a Party to reserve the right for the entirety of Article 4 not to apply to its Covered Tax  Agreements with Parties that have made the reservation described in paragraph 3(e). As a result of the  interaction between subparagraphs e) and f), paragraph 1 will be modified by the reservation under  paragraph 3(e) where one Contracting Jurisdiction to a Covered Tax Agreement has made the reservation  under paragraph 3(e), unless the other Contracting Jurisdiction has made the reservation under paragraph  3(f). As a result, all references to paragraph 1 throughout the Article would refer to paragraph 1 as it may  be modified by paragraph 3(e).

58.  It should be noted that because paragraph 1 explicitly denies the benefits of the Covered Tax  Agreement in the absence of an agreement between the competent authorities of the Contracting  Jurisdictions, the failure to grant such benefits cannot be viewed as taxation that is not in accordance with

the provisions of the Covered Tax Agreement. This would mean, for example, that cases in which benefits  are denied due to a failure of the competent authorities of the Contracting Jurisdictions to reach agreement  would not be eligible for arbitration under a Covered Tax Agreement that provides for arbitration of cases  of taxation that is not in accordance with the provisions of the Covered Tax Agreement.

Paragraph 4

59.  To ensure clarity about which existing provisions will be replaced by paragraph 1, paragraph 4  requires each Party (other than a Party that has reserved the right under paragraph 3(a) for the entirety of

Article 5 – Application of Methods for Elimination of Double Taxation

Paragraph 1

60.  Paragraphs 442 through 444 of the Action 2 Report describe three alternative ways in which  countries may address problems arising from the inclusion of the exemption method in treaties with respect  to items of income that are not taxed in the State of source. These alternatives are reflected in paragraphs 2  and 3 (Option A), paragraphs 4 and 5 (Option B) and paragraphs 6 and 7 (Option C) of Article 5. A Party  would be permitted to choose Option A, Option B, or Option C, or to choose to apply none of the options.  Recognising that asymmetrical application is commonplace in provisions relating to elimination of double  taxation, where the Contracting Jurisdictions to a Covered Tax Agreement each choose different options,  then by default, each Contracting Jurisdiction would be permitted to apply its chosen Option with respect  to its own residents (subject to paragraphs 8 and 9).

Option A

Paragraph 2

61.  Paragraph 2 is based on Article 23A(4) of the OECD Model Tax Convention, as described in  paragraph 444 (pages 146-147) and Note 1 (page 149) of the Action 2 Report, which reads as follow:

4. The provisions of paragraph 1 shall not apply to income derived or capital owned by a  resident of a Contracting State where the other Contracting State applies the provisions of  this Convention to exempt such income or capital from tax or applies the provisions of  paragraph 2 of Article 10 or 11 to such income.

62.  Changes were made to the model text of Article 23A(4) to conform the terminology used therein  to the terminology used in the Convention and to replace the reference to the provisions of paragraph 1 of  Article 23A with a more general reference to provisions for the elimination of double taxation. Changes  were also made to replace the references to “paragraph 2 of Article 10 or 11” of the OECD Model Tax  Convention with a more general reference to income taxed at a reduced rate, to accommodate Covered Tax  Agreements that allow for the application of withholding taxes to income other than dividends and interest,  such as income from royalties.

63.  Two sentences are also added to the end of the model provision to ensure that the addition of  Option A does not result in double taxation in the case of Covered Tax Agreements that do not already  provide for the credit method in the case of income subject to a reduced rate of tax at source.

Paragraph 3

64.  Paragraph 3 is the compatibility clause, which describes the interaction between Option A and  the provisions of Covered Tax Agreements. The compatibility clause indicates that Option A would apply  to Covered Tax Agreements that would otherwise require a Contracting Jurisdiction to exempt income that  the other Contracting Jurisdiction subjects to a reduced rate of tax or exempts based on its application of  the Covered Tax Agreement. This would apply, for example, to provisions of the type found in Article 23A  of the OECD and UN Model Tax Conventions, as well as provisions of Covered Tax Agreements  implementing the exemption method for the elimination of double taxation.

65.  Paragraph 3 of Option A should not be read to apply to provisions that grant exclusive taxing  rights to the Contracting Jurisdiction of residence with respect to specific types of income, such as  provisions that exempt dividends from source taxation.

Option B

Paragraph 4

66.  Option B allows Contracting Jurisdictions not to apply the exemption method with respect to  dividends that are deductible in the Contracting Jurisdiction of the payer, as described in paragraph 444  (pages 146-147) of the Action 2 Report. Option B reflects new drafting, as no provision implementing this  Option was drafted during the course of the work under Action 2. Option B is intended to address a  situation in which income derived by a resident of a Contracting Jurisdiction that would otherwise be  treated under the Covered Tax Agreement as exempt dividend income in that Contracting Jurisdiction is  treated as a deductible payment by the other Contracting Jurisdiction.

Paragraph 5

67.  Paragraph 5 is the compatibility clause, which describes the interaction between Option B and the  provisions of Covered Tax Agreements. The compatibility clause indicates that Option B would apply to  Covered Tax Agreements that would otherwise require a Contracting Jurisdiction to exempt income  derived by its residents from dividends that are deductible in the Contracting Jurisdiction of the payer.

Option C

Paragraph 6

68.  Option C reflects the credit method for the elimination of double taxation and is based on Article  23B of the OECD Model Tax Convention, as updated by the BEPS Project, which reads as follow:

1.  Where a resident of a Contracting State derives income or owns capital which may be  taxed in the other Contracting State in accordance with the provisions of this Convention  (except to the extent that these provisions allow taxation by that other State solely because  the income is also income derived by a resident of that State), the first-mentioned State shall  allow:

a)  as a deduction from the tax on the income of that resident, an amount equal to  the income tax paid in that other State;

b)  as a deduction from the tax on the capital of that resident, an amount equal to  the capital tax paid in that other State.    Such deduction in either case shall not, however, exceed that part of the income tax or  capital tax, as computed before the deduction is given, which is attributable, as the case may  be, to the income or the capital which may be taxed in that other State.

2.  Where in accordance with any provision of the Convention income derived or capital  owned by a resident of a Contracting State is exempt from tax in that State, such State may  nevertheless, in calculating the amount of tax on the remaining income or capital of such  resident, take into account the exempted income or capital.

69.  The sole changes to the model text are made to conform the terminology used therein to the  terminology used in the Convention.

Paragraph 7

70.  Paragraph 7 is the compatibility clause, which describes the interaction between Option C and the  provisions of Covered Tax Agreements. The compatibility clause indicates that Option C would apply in  place of provisions of a Covered Tax Agreement that, for the purposes of eliminating double taxation,  require a Contracting Jurisdiction to exempt from tax in that Contracting Jurisdiction income derived or  capital owned by a resident of that Contracting Jurisdiction which, in accordance with the provisions of the  Covered Tax Agreement, may be taxed in the other Contracting Jurisdiction.

71.  Paragraph 7 should not be read to replace existing provisions intended to clarify that dividends  that would be exempt from tax under the domestic law of the Contracting Jurisdiction of residence would  be exempt under the Covered Tax Agreement as well.

Paragraphs 8 and 9

72.  As noted above, by default, where one Party chooses to apply Option A, B, or C to its Covered  Tax Agreements, and the other Party chooses a different Option (or chooses not to apply an Option), each  Party’s choice would apply with respect to its own residents. Some members of the ad hoc Group have  expressed the concern, however, that accepting asymmetrical application across the board could disrupt the  balance of certain bilateral tax treaties where the provision on the elimination of double taxation was the  subject of bilateral compromise. To address these concerns, paragraph 8 allows a Party that does not  choose to apply an Option under paragraph 1 of this Article to reserve the right for the entirety of Article 5  not to apply with respect to one or more identified Covered Tax Agreements, or with respect to all of its  Covered Tax Agreements.

73.  Some Parties may be comfortable with asymmetrical application of Option A or B, which  represent incremental changes to deal with cases of conflict of qualifications, but may prefer to address  more significant changes, such as those reflected in Option C, through bilateral negotiation. To permit that  approach, paragraph 9 allows a Party that does not choose to apply Option C to choose, with respect to one  or more identified Covered Tax Agreements (or with respect to all of its Covered Tax Agreements), not to  permit the other Contracting Jurisdiction to apply Option C.

Paragraph 10

74.  Paragraph 10 requires each Party that has chosen to apply an Option under paragraph 1 to notify  the Depositary of 1) its choice of Option, 2) each Covered Tax Agreement containing a provision within  the scope of the compatibility clause for that Option; and 3) the article and paragraph number of each such  provision. To ensure clarity, an Option will only apply with respect to a provision of a Covered Tax  Agreement if the Party that chose to apply the Option makes such a notification with respect to that  provision.

Part III. Treaty Abuse

Article 6 – Purpose of a Covered Tax Agreement

75.  The minimum standard for protection against the abuse of tax treaties under Action 6 (Preventing  the Granting of Treaty Benefits in Inappropriate Circumstances) requires countries to include in their tax  treaties an express statement that their common intention is to eliminate double taxation without creating  opportunities for non-taxation or reduced taxation through tax evasion or avoidance, including through  treaty-shopping arrangements. This could be done by including such a statement in the preambles of tax  treaties. For this purpose, model preamble text was produced in paragraph 72 (page 92) of the Action 6  Report, which reads:

(State A) and (State B),

Desiring to further develop their economic relationship and to enhance their co-operation  in tax matters,

Intending to conclude a Convention for the elimination of double taxation with respect to  taxes on income and on capital without creating opportunities for non-taxation or reduced  taxation through tax evasion or avoidance (including through treaty-shopping  arrangements aimed at obtaining reliefs provided in this Convention for the indirect benefit  of residents of third States)

Have agreed as follows:

76.  While this text is added to the preamble of a Covered Tax Agreement after the original  conclusion, the intent of the Contracting Jurisdictions is that the Covered Tax Agreement would be  interpreted in line with the purpose of the Covered Tax Agreement described in the preamble text. In this  regard, the penultimate paragraph of the preamble of the Convention also confirms the need to ensure that  existing agreements for the avoidance of double taxation on income (whether or not other taxes are also  covered) are interpreted to eliminate double taxation with respect to the taxes covered by those agreements  without creating opportunities for non-taxation or reduced taxation through tax evasion or avoidance  (including through treaty-shopping arrangements aimed at obtaining reliefs provided in those agreements  for the indirect benefit of residents of third jurisdictions).

Paragraph 1

77.  Paragraph 1 provides that the Convention modifies a Covered Tax Agreement to include  preamble language stating that the purpose of the Covered Tax Agreement is to eliminate double taxation  without creating opportunities for non-taxation or reduced taxation through tax evasion or avoidance,  including through treaty-shopping arrangements.

78.  Reflecting the fact that the statement will be incorporated into Covered Tax Agreements after  their original conclusion, the model language “Intending to conclude a Convention for the elimination of  double taxation” has been replaced with “Intending to eliminate double taxation”. In addition, the phrase  “taxes on income and on capital” has been replaced with “taxes covered by this agreement” to address  Covered Tax Agreements that cover additional taxes or use different phrasing for the taxes covered.

79.  With respect to the title of tax treaties, some Covered Tax Agreements use the term “Convention”,  while others use “Agreement”. In this regard, the term “Convention” in the model text has been replaced

with the broader term “agreement” to ensure that a Covered Tax Agreement would be covered regardless  of its title.

80.   In addition, the French version of the preamble text that will be included in Covered Tax  Agreements has been modified to take into account different French equivalents of the English term “tax  avoidance”. To accommodate jurisdictions for which the term “tax avoidance ” is translated into French as  “évitement fiscal”, the French version of Article 6 includes in paragraphs 1 and 4 the term “évitement  fiscal” immediately after the term “fraude fiscale”. To make the reason for this addition clear, the preamble  text that will be included in Covered Tax Agreements in French also includes a footnote stating that certain  jurisdictions translate the English term “tax avoidance” as “évitement fiscal”.

Paragraph 2

81.  Paragraph 2 is a compatibility clause which describes the interaction between paragraph 1 and the  preamble language of Covered Tax Agreements. This paragraph clarifies that the preamble text in  paragraph 1 replaces existing preamble language of Covered Tax Agreements that refers to an intent to  eliminate double taxation (whether or not that language also refers to an intent not to create opportunities  for non-taxation or reduced taxation), or is added to the preamble of Covered Tax Agreements where such  language does not exist in the preamble of the Covered Tax Agreements.

82.  Some Covered Tax Agreements may contain preamble language that refers to an intent to  eliminate double taxation without creating opportunities for non-taxation or reduced taxation but does not  include a reference to tax evasion or avoidance or to treaty shopping. Paragraph 1 is intended to cover  these examples and replace them with the preamble language in paragraph 1, though such language may be  preserved through the reservation set out in paragraph 4.

Paragraph 3

83.  Some Parties may prefer to include the full preamble language produced in the Action 6 Report  rather than only the portion related to the elimination of double taxation without creating opportunities for  non-taxation or reduced taxation through tax evasion or avoidance. Paragraph 3 allows the possibility to  include the other part of the preamble of the OECD Model Tax Convention:

Desiring to further develop their economic relationship and to enhance their co-operation  in tax matters,

84.  Paragraph 3 provides that this preamble language is included only with respect to Covered Tax  Agreements that do not already contain preamble language referring to a desire to develop an economic  relationship or to enhance co-operation in tax matters. Also, given that including this portion of the  preamble of the OECD Model Tax Convention is not required in order to meet a minimum standard, this  paragraph is an optional provision, and, as provided in paragraph 6, will modify a Covered Tax Agreement  only where all Contracting Jurisdictions agree to such modification by choosing to apply paragraph 3.

Paragraph 4

85.  Because paragraph 1 reflects the minimum standard for protection against the abuse of tax  treaties under Action 6, paragraph 4 permits a Party to opt out of applying paragraph 1 only with respect to  Covered Tax Agreements that already satisfy the minimum standard. Paragraph 4 is intended to permit  Parties to preserve preamble language in their Covered Tax Agreements that already refers to the intent to  eliminate double taxation without creating opportunities for non-taxation or reduced taxation, whether or

not such language is limited to cases of tax evasion or avoidance (including cases of treaty shopping) or  applies more broadly.

Paragraph 5

86.  To ensure clarity about which existing preamble language will be replaced by the text described  in paragraph 1, paragraph 5 requires each Party to notify the Depositary of whether each of its Covered  Tax Agreements, other than those that are within the scope of a reservation under paragraph 4, contains  preamble language referring to an intent to eliminate double taxation, and if so, the text of the relevant  preambular paragraph. Existing preamble language would be replaced by the text described in paragraph 1  where all Contracting Jurisdictions have made such a notification with respect to the existing preamble  language. In other cases, the text described in paragraph 1 would be included in addition to the existing  preamble language. To avoid unexpected mismatches in notification, each Party making a notification with  respect to a preambular paragraph may also clarify whether the relevant preambular paragraph also  includes text that is not described in paragraph 2 (with the exception of minor variations). Such text would  not be modified by paragraph 1.

Paragraph 6

87.  Paragraph 6 requires each Party that chooses to apply paragraph 3 to notify the Depositary of its  choice. To ensure clarity about whether the text described in paragraph 3 will be included in a particular  Covered Tax Agreement, such notification shall also include the list of its Covered Tax Agreements that do  not already contain preamble language referring to a desire to develop an economic relationship or to  enhance co-operation in tax matters. The text described in paragraph 3 will be included in a Covered Tax  Agreement only where all Contracting Jurisdictions have chosen to apply that paragraph and have made  such a notification with respect to the Covered Tax Agreement.

Article 7 – Prevention of Treaty Abuse

88.  The Action 6 Report includes three alternative rules to address situations of treaty abuse. The first  of these alternatives is a general anti-abuse rule based on the principal purpose of transactions or  arrangements. In addition to this principal purpose test (PPT), the Action 6 Report provides two versions (a  simplified and detailed version) of a specific anti-abuse rule, the limitation on benefits (LOB) provision,  which limits the availability of treaty benefits to persons that meet certain conditions.

89.  Paragraph 22 (page 19) of the Action 6 Report states that countries, at a minimum, should  implement: (i) a PPT only; (ii) a PPT and either a simplified or detailed LOB provision; or (iii) a detailed  LOB provision, supplemented by a mechanism that would deal with conduit arrangements not already  dealt with in tax treaties.

90.  Because a PPT is the only approach that can satisfy the minimum standard on its own, it is  presented as the default option in paragraph 1. Parties are then permitted pursuant to paragraph 6 to  supplement the PPT by choosing to apply a simplified LOB provision. Given that the detailed LOB  provision requires substantial bilateral customisation, which would be challenging in the context of a  multilateral instrument, the Convention does not include a detailed LOB provision. Instead, Parties that  prefer to address treaty abuse by adopting a detailed LOB provision are permitted to opt out of the PPT and  agree instead to endeavour to reach a bilateral agreement that satisfies the minimum standard. Also, given  that Parties preferring a detailed LOB provision may accept the PPT in paragraph 1 as an interim measure,  paragraph 17(a) allows such Parties to express the intent in the notification under that paragraph.

Paragraph 1

91.  Paragraph 1 includes the PPT, which is based on paragraph 7 of Article X (Entitlement to  Benefits) of the OECD Model Tax Convention produced in paragraph 26 (page 55) of the Action 6 Report.  The model provision reads as follows:

7.  Notwithstanding the other provisions of this Convention, a benefit under this  Convention shall not be granted in respect of an item of income or capital if it is reasonable  to conclude, having regard to all relevant facts and circumstances, that obtaining that  benefit was one of the principal purposes of any arrangement or transaction that resulted  directly or indirectly in that benefit, unless it is established that granting that benefit in  these circumstances would be in accordance with the object and purpose of the relevant  provisions of this Convention.

92.  The sole changes to the model provision are to conform the terminology used in the model  provision to the terminology used in the Convention.

Paragraph 2

93.  Paragraph 2 is a compatibility clause which describes the interaction between paragraph 1 and  provisions of Covered Tax Agreements. This paragraph clarifies that the PPT in paragraph 1 replaces  existing provisions of Covered Tax Agreements that deny all or part of the benefits otherwise provided  under the Covered Tax Agreement where the principal purpose or one of the principal purposes of any  arrangement or transaction, or of the parties to an arrangement or transaction, was to obtain those benefits,  or is added where such provisions do not exist in Covered Tax Agreements.

94.  Existing PPTs vary in terms of whether they cover all benefits of Covered Tax Agreements or  only the benefits under specific articles such as dividends, interest, royalties, income from employment,  other income and elimination of double taxation. In this regard, the reference in paragraph 2 to provisions  that deny “all or part of the benefits” is intended to ensure that narrower provisions will also be replaced  with the broader provision in paragraph 1.

95.  Existing PPTs that use similar terms, such as “main purpose” or “primary purpose” are also  intended to be covered by the phrase “principal purpose” in this paragraph. While Covered Tax  Agreements may already contain various types of anti-abuse rules other than a PPT, the PPT in paragraph  1 is not intended to restrict the scope or application of such existing anti-abuse rules.

96.  Some existing PPTs may include existing procedural requirements such as notification or  consultation between the competent authorities when the PPTs are applied. The compatibility clause in  paragraph 2 would replace the existing PPTs including such notification or consultation provisions.

Paragraphs 3 and 4

97.  Paragraph 16 of the Commentary on the PPT in the Action 6 Report (pages 64 and 65) noted that  countries are free to include in their bilateral tax treaties the following additional paragraph:

8.  Where a benefit under this Convention is denied to a person under paragraph 7, the  competent authority of the Contracting State that would otherwise have granted this benefit  shall nevertheless treat that person as being entitled to this benefit, or to different benefits  with respect to a specific item of income or capital, if such competent authority, upon

request from that person and after consideration of the relevant facts and circumstances,  determines that such benefits would have been granted to that person in the absence of the  transaction or arrangement referred to in paragraph 7. The competent authority of the  Contracting State to which the request has been made will consult with the competent  authority of the other State before rejecting a request made under this paragraph by a  resident of that other State.

98.  Paragraph 3 permits Parties that have not opted out of the PPT under paragraph 15(a) to choose  to include the additional provision in Covered Tax Agreements. Paragraph 4 reflects the additional  provision with minor changes (to conform terminology and to avoid cross-references to a particular article  by number). Paragraph 4 is an optional provision, and, as provided in paragraph 17(b), will apply to a  Covered Tax Agreement only where all Contracting Jurisdictions have chosen to apply it by making a  notification under paragraph 17(b).

Paragraph 5

99.  Paragraph 5 is a compatibility clause which describes the interaction between paragraph 4 and  provisions of Covered Tax Agreements. This paragraph clarifies that when the Contracting Jurisdictions to  a Covered Tax Agreement have chosen to apply paragraph 4, it will be applied to a PPT of a Covered Tax  Agreement (as it may be modified by the Convention). In general, an existing PPT will be modified by  paragraph 1, with the result that in practice, paragraph 4 will apply in conjunction with paragraph 1.

Paragraph 6

100.  Paragraph 6 allows Parties to choose to apply the simplified LOB provision contained in  paragraphs 8 through 13 (the “Simplified Limitation on Benefits Provision”) as a supplement to the PPT in  paragraph 1 by making the notification described in paragraph 17(c). The Simplified Limitation on  Benefits Provision is an optional provision, and applies with respect to a Covered Tax Agreement only  where all Contracting Jurisdictions have chosen to apply it. As exceptions to the rule, the Simplified  Limitation on Benefits Provision could still apply with respect to a Covered Tax Agreement for which  some but not all of the Contracting Jurisdictions have chosen pursuant to paragraph 6 to apply the  Simplified Limitation on Benefits Provision, provided that there is agreement under paragraph 7(a) or (b).

Paragraph 7

101.  Where one Party chooses to apply the Simplified Limitation on Benefits Provision pursuant to  paragraph 6 and the other does not, the Simplified Limitation on Benefits Provision would not apply, and  by default, the PPT in paragraph 1 would apply symmetrically. Parties that choose to apply the Simplified  Limitation on Benefits Provision are, however, permitted under paragraph 16 to opt out of the entirety of

102.  Subparagraph a) allows Parties that choose to apply the PPT alone to agree that the Simplified  Limitation on Benefits Provision would apply symmetrically for the purposes of granting benefits in the  case of Covered Tax Agreements with Parties that choose to apply the Simplified Limitation on Benefits  Provision. Subparagraph b), in contrast, allows Parties that choose to apply the PPT alone to permit the  Simplified Limitation on Benefits Provision to be applied asymmetrically with respect to a Covered Tax  Agreement. Under subparagraph b), a Contracting Jurisdiction to a Covered Tax Agreement that chooses  to apply the Simplified Limitation on Benefits Provision would apply the PPT and the Simplified

Limitation on Benefits Provision in determining whether to grant the benefits of the Covered Tax  Agreement, while the other Contracting Jurisdiction that does not choose to apply the Simplified  Limitation on Benefits Provision would apply the PPT alone in determining whether to grant treaty  benefits. This agreement on the application of the Simplified Limitation on Benefits Provision is done by  choosing to apply subparagraph a) or b) and notifying the Depositary accordingly under paragraph 17(d).

103.  If a Contracting Jurisdiction to a Covered Tax Agreement that prefers to apply the PPT alone  does not affirmatively agree to the application of the Simplified Limitation on Benefits Provision under  subparagraph a) or b), the exceptions under this paragraph would not apply with respect to the Covered  Tax Agreement. In such a case, the PPT alone would apply, subject to paragraph 16.

Paragraphs 8 through 13 – Simplified Limitation on Benefits Provision

104.  Paragraphs 8 through 13 contain a simplified LOB provision, based on paragraphs 1 through 6 of  Article X (Entitlement to Benefits) of the OECD Model Tax Convention produced in paragraph 25 (page  21) of the Action 6 Report and finalised in the course of follow-up work by OECD CFA Working Party  No.1 on Tax Conventions and Related Questions (WP1). The version of the provision produced by WP1 as  it stood when the Convention was developed reads as follows:

1.  Except as otherwise provided in this Article, a resident of a Contracting State shall  not be entitled to a benefit that would otherwise be accorded by this Convention (other than  a benefit under paragraph 3 of Article 4, paragraph 2 of Article 9 or Article 25), unless such  resident is a “qualified person”, as defined in paragraph 2 at the time that the benefit would  be accorded.

2.  A resident of a Contracting State shall be a qualified person at a time when a benefit  would otherwise be accorded by the Convention if, at that time, the resident is:

a)  an individual;

b)  that Contracting State, or a political subdivision or local authority thereof, or  an agency or instrumentality of any such Contracting State, political  subdivision or local authority;

c)  a company or other entity, if the principal class of its shares is regularly traded  on one or more recognised stock exchanges;

d)  a person, other than an individual, that

i)  is a [agreed description of the relevant non-profit organisations found in  each Contracting State]; or

ii)  is a recognised pension fund

e)  a person other than an individual, if, on at least half the days of a twelve-month  period that includes the time when the benefit otherwise would be accorded,  persons who are residents of that Contracting State and that are entitled to  benefits of this Convention under subparagraphs a) to d) own, directly or  indirectly, at least 50 per cent of the shares of the person

3.  a)  A resident of a Contracting State will be entitled to benefits of this Convention  with respect to an item of income derived from the other Contracting State,  regardless of whether the resident is a qualified person, if the resident is  engaged in the active conduct of a business in the first-mentioned Contracting  State, and the income derived from the other Contracting State emanates from  or is incidental to, that business. For purposes of this Article, the term “active  conduct of a business” shall not include the following activities or any  combination thereof:

i)  operating as a holding company;

ii)  providing overall supervision or administration of a group of companies;

iii)  providing group financing (including cash pooling); or

iv)  making or managing investments, unless these activities are carried on  by a bank, insurance company or registered securities dealer in the  ordinary course of its business as such.

b)  If a resident of a Contracting State derives an item of income from a business  activity conducted by that resident in the other Contracting State, or derives an  item of income arising in the other State from a connected person, the  conditions described in subparagraph a) shall be considered to be satisfied with  respect to such item only if the business activity carried on by the resident in the  first-mentioned State to which the item is related is substantial in relation to the  same or complementary business activity carried on by the resident or such  connected person in the other Contracting State. Whether a business activity is  substantial for the purposes of this paragraph shall be determined based on all  the facts and circumstances.

c)  For purposes of applying this paragraph, activities conducted by connected  persons with respect to a resident of a Contracting State shall be deemed to be  conducted by such resident.

4.  A resident of a Contracting State that is not a qualified person shall also be entitled to  a benefit that would otherwise be accorded by this Convention with respect to an item of  income if, on at least half of the days of any twelve-month period that includes the time  when the benefit otherwise would be accorded, persons that are equivalent beneficiaries  own, directly or indirectly, at least 75 per cent of the beneficial interests of the resident.

5.  If a resident of a Contracting State is neither a qualified person pursuant to the  provisions of paragraph 2 of this Article, nor entitled to benefits under paragraph 3 or 4 of  this Article, the competent authority of the other Contracting State may, nevertheless, grant  the benefits of this Convention, or benefits with respect to a specific item of income, taking  into account the object and purpose of this Convention, but only if such resident  demonstrates to the satisfaction of such competent authority that neither its establishment,

acquisition or maintenance, nor the conduct of its operations had as one of its principal  purposes the obtaining of benefits under this Convention. The competent authority of the  Contracting State to which a request has been made shall consult with the competent  authority of the other State before either granting or denying the request made under this  paragraph by a resident of that other State.

6.  For the purposes of this Article:

a)  the term “recognised stock exchange” means:

i)  any stock exchange established and regulated as such under the laws of  either Contracting State; and

ii)  any other stock exchange agreed upon by the competent authorities of  the Contracting States;

b)  the term “principal class of shares” means the class or classes of shares of a  company which represents the majority of the aggregate vote and value of the  company or the class or classes of beneficial interests of an entity which  represents in the aggregate a majority of the aggregate vote and value of the  entity;

c)  the term “equivalent beneficiary” means any person who would be entitled to  benefits with respect to an item of income accorded by a Contracting State  under the domestic law of that Contracting State, this Convention or any other  international instrument which are equivalent to, or more favourable than,  benefits to be accorded to that item of income under this Convention. For the  purposes of determining whether a person is an equivalent beneficiary with  respect to dividends, the person shall be deemed to hold the same capital of the  company paying the dividends as such capital the company claiming the benefit  with respect to the dividends holds;

d)  with respect to entities that are not companies, the term “shares” means  interests that are comparable to shares;

e)  two persons shall be “connected persons” if one owns, directly or indirectly, at  least 50 percent of the beneficial interest in the other (or, in the case of a  company, at least 50 percent of the aggregate vote and value of the company's  shares) or another person owns, directly or indirectly, at least 50 percent of the  beneficial interest (or, in the case of a company, at least 50 percent of the  aggregate vote and value of the company's shares) in each person. In any case,  a person shall be connected to another if, based on all the relevant facts and  circumstances, one has control of the other or both are under the control of the  same person or persons.

105.  Like other provisions produced as part of the BEPS work for inclusion in the OECD Model Tax  Convention, the model provision has been modified for inclusion in the Convention. In particular, the  terminology has been adjusted to match the terminology used in the Convention, and the references to  particular paragraphs and articles by number have been replaced with descriptive language.

106.  In addition, the model provision contemplates bilateral negotiation of the non-profit organisations  to be treated as qualified persons in paragraph 2(d)(i). While it was considered that in general, requiring  bilateral negotiation would not be appropriate in the context of a multilateral instrument, given that it was  not anticipated that the Simplified Limitation on Benefits Provision would be adopted by all Parties to the  Convention, paragraph 9(d)(i) permits Parties to agree bilaterally on the non-profit organisations to be  covered through an exchange of diplomatic notes.

107.  The model provision also refers to the defined term “recognised pension funds” in paragraph  2(d)(ii). Rather than using this defined term, paragraph 9(d)(ii) has incorporated the content of the  definition.

Paragraph 14

108.  Paragraph 14 is a compatibility clause which describes the interaction between the Simplified  Limitation on Benefits Provision and provisions of Covered Tax Agreements. The Simplified Limitation  on Benefits Provision would replace existing provisions of Covered Tax Agreements that would limit the  benefits of the Covered Tax Agreements (or that would limit benefits other than a benefit under the articles  relating to residence, associated enterprises or non-discrimination or a benefit that is not restricted solely to  residents of a Contracting Jurisdiction) only to a resident that qualifies for such benefits by meeting one or  more categorical tests, or would be added where such provisions do not exist in Covered Tax Agreements.  Thus, it is intended to apply in place of or in the absence of existing LOB provisions. It is not, however,  intended to restrict the scope or application of other types of anti-abuse rules in Covered Tax Agreements.

Paragraph 15

109.  Paragraph 15 defines the reservations that are permitted from Article 7. Subparagraph a) allows  Parties that intend to satisfy the minimum standard by adopting a combination of a detailed LOB provision  and either rules to address conduit financing structures or a PPT to opt out of including the PPT in  paragraph 1 in their Covered Tax Agreements. To ensure that Parties that opt out of the PPT under this  paragraph will still have an avenue to meet the minimum standard, this subparagraph requires the  Contracting Jurisdictions to endeavour to reach a mutually satisfactory solution which is in line with the  minimum standard. Given that there are multiple measures to meet the minimum standard under Action 6,  and that reaching a mutually satisfactory solution solely through the efforts of one Contracting Jurisdiction  would not be possible, this paragraph requires not only the reserving Party but also the other Contracting  Jurisdiction to the relevant Covered Tax Agreement to endeavour to reach a mutually satisfactory solution  that is in line with the minimum standard.

110.  While subparagraph a) refers to “the OECD/G20 BEPS package” in order to identify the  minimum standard for preventing treaty abuse, the obligation imposed on the Contracting Jurisdictions is  to use their best efforts to reach bilateral agreement on a provision that is consistent with the agreed  minimum standard. It is not meant to suggest that any legal obligations are imposed by the BEPS package.  The term “a detailed limitation on benefits provision” in paragraph 15(a) refers to a detailed provision of  the type appearing in paragraphs 1 through 6 of Article X (Entitlement to Benefits) of the OECD Model  Tax Convention produced in paragraph 25 (page 21) of the Action 6 Report, which will be further  developed in the course of the follow-up work on BEPS. The term “a principal purpose test” means a  provision of the type described in paragraph 1.

111.  Subparagraph b) allows Parties to opt out of paragraph 1 (and paragraph 4, where the Parties  have chosen to apply it) with respect to Covered Tax Agreements that already contain a PPT. This would  apply only with respect to a comprehensive PPT denying all treaty benefits, and would not apply to a PPT- type test that applies only with respect to benefits under specific articles such as dividends, interest,  royalties, income from employment, other income and elimination of double taxation.

112.  Subparagraph c) allows Parties to opt out of the Simplified Limitation on Benefits Provision with  respect to Covered Tax Agreements that already contain an LOB provision described in paragraph 14.  Parties that do not choose pursuant to paragraph 6 to apply the Simplified Limitation on Benefits Provision  but accept its symmetrical or asymmetrical application pursuant to paragraph 7 may prefer to opt out of the  Simplified Limitation on Benefits Provision with respect to Covered Tax Agreements that already contain  an LOB provision. Therefore, paragraph 15(c) would be available to such Parties as well as Parties that  choose pursuant to paragraph 6 to apply the Simplified Limitation on Benefits Provision.

Paragraph 16

113.  As described above with respect to paragraphs 6 and 7, where one Contracting Jurisdiction to a  Covered Tax Agreement prefers to apply the PPT in paragraph 1 alone and the other Contracting  Jurisdiction prefers to apply the PPT combined with the Simplified Limitation on Benefits Provision, the  Simplified Limitation on Benefits Provision would not apply (unless there is agreement under paragraph  7(a) or (b)). In such cases, Parties that prefer to apply the Simplified Limitation on Benefits Provision may  prefer to apply nothing under Article 7 and leave the issue to bilateral negotiations. Where the Contracting  Jurisdiction preferring the PPT alone has not chosen to apply paragraph 7(a) or (b), paragraph 16 therefore  allows Parties that choose pursuant to paragraph 6 to apply the Simplified Limitation on Benefits Provision  to opt out of Article 7 entirely with respect to their Covered Tax Agreements. To ensure that the  Contracting Jurisdictions to Covered Tax Agreements for which the entirety of Article 7 is opted out of  under this paragraph will still have an avenue to meet the minimum standard, this paragraph, like  paragraph 15(a), requires them to endeavour to reach a mutually satisfactory solution which is in line with  the minimum standard.

Paragraph 17

114.  Paragraph 17 describes notifications that are required in order to ensure clarity as to the  application of Article 7. Subparagraph a) requires Parties that have not opted out of the application of  paragraph 1 under paragraph 15(a) to notify the Depositary of each of its Covered Tax Agreements that is  not subject to a reservation under paragraph 15(b) and that contains an existing PPT, along with the article  and paragraph number of each such provision. An existing provision of a Covered Tax Agreement would  be replaced by the provisions of paragraph 1 (and paragraph 4, where applicable) where all Contracting  Jurisdictions to that Covered Tax Agreement have made such a notification with respect to the existing  provision. In other cases, paragraph 1 (and paragraph 4, where applicable) would apply to the Covered Tax  Agreement, but would supersede the existing provisions of the Covered Tax Agreement only to the extent  that those provisions are incompatible with paragraph 1 (and where applicable, paragraph 4).

115.  Given the fact that not all of the possible ways to meet the minimum standard under Action 6 are  provided by the Convention, some Parties may choose to apply the PPT provided in paragraph 1 alone as  an interim measure, with the intent, where possible, of adopting other measures to satisfy the minimum  standard through bilateral negotiations. To ensure clarity, a Party making a notification under subparagraph  a) may also express such intent. Such Parties may then seek, through bilateral negotiation, to adopt a  simplified or detailed LOB provision to supplement paragraph 1, or to replace paragraph 1 with a detailed  LOB provision supplemented by rules to address conduit financing structures.

116.  Subparagraphs b) through d) require Parties that choose to apply optional provisions of Article 7  (i.e. paragraph 4, paragraph 6, and paragraph 7(a) or (b)) to notify the Depositary of their choices in order  to clarify which Parties choose those optional provisions.

117.  With respect to subparagraphs c) and d), unless the Party that makes a notification of its choice  for the application of the Simplified Limitation on Benefits Provision under those subparagraphs has made  the reservation described in paragraph 15(c), such Party shall also notify of the list of its Covered Tax  Agreements that contain a provision described in paragraph 14, as well as the article and paragraph number  of each such provision. Subparagraph e) ensures clarity about which existing provisions will be replaced  by the Simplified Limitation on Benefits Provision. An existing provision of a Covered Tax Agreement  would be replaced by the Simplified Limitation on Benefits Provision where all Contracting Jurisdictions  have made such a notification under subparagraph c) or d) with respect to the existing provision. In other  cases, the Simplified Limitation on Benefits Provision would apply to the Covered Tax Agreement, but  would supersede the existing provisions of the Covered Tax Agreement only to the extent that those  provisions are incompatible with the Simplified Limitation on Benefits Provision. In the case where  paragraph 7(b) applies, such modification would be made asymmetrically only with respect to the  application of the Simplified Limitation on Benefits Provision by the Contracting Jurisdiction that has  chosen pursuant to paragraph 6 to apply the Simplified Limitation on Benefits Provision.

Article 8 – Dividend Transfer Transactions

Paragraph 1

118.  Paragraph 1 requires that a minimum shareholding period be satisfied in order for a company to  be entitled to a reduced rate on dividends from a subsidiary, based on Article 10(2) of the OECD Model  Tax Convention as revised in paragraph 36 (pages 70 and 71) of the Action 6 Report. The model provision  reads:

a)  5 per cent of the gross amount of the dividends if the beneficial owner is a company  (other than a partnership) which holds directly at least 25 per cent of the capital of  the company paying the dividends throughout a 365 day period that includes the day  of the payment of the dividend (for the purpose of computing that period, no account  shall be taken of changes of ownership that would directly result from a corporate  reorganisation, such as a merger or divisive reorganisation, of the company that  holds the shares or that pays the dividend);

119.  The provision of paragraph 1 has been modified to add language describing the situation in which  a minimum shareholding period needs to be introduced. Specifically, a minimum shareholding period is  added to provisions of a Covered Tax Agreement that exempt or limit taxation in one Contracting  Jurisdiction of dividends paid to a company which is a resident of the other Contracting Jurisdiction and  which holds more than a certain amount of the capital or voting power of the company paying the  dividends. Therefore, this paragraph does not affect existing provisions that give a preferential rate for  dividends without the condition on holding a certain amount of the capital of the company paying the  dividends.

120.  Also, recognising that the purpose of this provision is solely to introduce a minimum  shareholding period and not to change the substantive allocation of taxation rights between the Contracting  Jurisdictions to Covered Tax Agreements, language relating to the specific tax rate and ownership  threshold provided by the model provision has been deleted.

121.  In addition, given the variations of existing dividends provisions of Covered Tax Agreements, the  following changes have been made to the provision in paragraph 1. The terms “own” and “control” have  been added to address existing provisions that use those terms instead of “hold”.

(i)  The phrase “more than a certain amount” has been used to cover existing provisions  regardless of whether they use the phrase “at least [X] percent” or “more than [X] percent”.

(ii)  The term “recipient” has been added to address existing provisions that use that term instead  of “beneficial owner”. There may be a variety of examples other than “beneficial owner” or  “recipient”. Some existing provisions may use the terms “beneficiary”, “owner” or “receiving  company”, and others may refer to dividends “beneficially owned by”, “paid to”, “distributed  to” or “received by” a parent company, or a parent company “beneficially entitled” to  dividends. In this regard, it is intended that all of these examples would be covered by  “beneficial owner” or “recipient”.

(iii) The term “capital” also has a lot of variations such as “equity capital”, “authorised capital”,  “share capital”, “statutory capital”, “shares”, “shares representing … per cent of the  capital/voting power”, “outstanding shares of the voting stock”, “voting shares”, “capital  stock”, “voting stock”, “voting power”, “voting rights”, “control” and “participation  substantielle”. To address all of these variations, the phrase “capital, shares, stock, voting  power, voting rights or similar ownership interests” has been used in the provisions of  paragraph 1.

122.  Paragraph 1 is intended to add a minimum shareholding period to existing provisions of Covered  Tax Agreements without modifying the other elements of such provisions, such as tax rates, ownership  thresholds and form of ownership (e.g. directly and/or indirectly). This paragraph also would not modify  any other conditions, such as provisions requiring that:

•  the amount of investment is more than a certain monetary value;

•  profits out of which dividends are paid are subject to tax in the residence jurisdiction; or

•  not more than a certain amount of the gross income of the paying company consists of interest or  dividends.

123.  Some Covered Tax Agreements between EU members may contain a compatibility clause  providing that the EU Parent/Subsidiary Directive shall prevail over existing dividends provisions. The  Directive is designed to eliminate tax obstacles in the area of profit distributions between associated  companies of different EU members, and eliminates withholding taxes on dividends paid by the subsidiary  company to the parent company under some conditions. As described above, this paragraph just adds a  minimum shareholding period to existing dividends provisions, and would not repeal the provisions of  Covered Tax Agreements addressing compatibility with the Directive.

Paragraph 2

124.  Paragraph 2 describes the interaction between paragraph 1 and provisions of Covered Tax  Agreements. This paragraph clarifies that the 365 day minimum shareholding period in paragraph 1  replaces the minimum shareholding periods already contained in provisions of Covered Tax Agreements,  or is added where such periods do not exist in provisions of Covered Tax Agreements. If Parties prefer to  preserve existing minimum shareholding periods, paragraph 3(b) allows the possibility to opt out of Article

8 with respect to provisions of Covered Tax Agreements that already include a minimum shareholding  period.

Paragraph 3

125.  Given that a provision addressing dividend transfer transactions is not required in order to meet a  minimum standard, paragraph 3(a) allows Parties to opt out of Article 8 entirely.

126.  Subparagraph b)(i) allows Parties to opt out of Article 8 entirely with respect to Covered Tax  Agreements to the extent that the provisions described in paragraph 1 already include a minimum  shareholding period. This reservation is intended to apply on a provision basis instead of on an agreement  basis. As a result, if a Covered Tax Agreement contains the provisions described in paragraph 1 that  provide two split rates, and one includes a minimum shareholding period and the other does not, this clause  would preserve the first provisions alone, while paragraph 1 would add a minimum shareholding period to  the latter provisions. In addition, subparagraph b)(ii) and (iii) allow a Party to choose to preserve a  minimum shareholding period included in provisions of a Covered Tax Agreement that is shorter or longer  than 365 days.

Paragraph 4

127.  To ensure clarity about the application of Article 8, paragraph 4 requires each Party (other than a  Party that has reserved the right under paragraph 3(a) for the entirety of Article 8 not to apply to all of its  Covered Tax Agreements) to notify the Depositary of whether each of its Covered Tax Agreements  contains a provision described in paragraph 1 that is not subject to a reservation described in paragraph 3  (b), and if so, the article and paragraph number of each such provision. Paragraph 1 would apply with  respect to an existing provision of a Covered Tax Agreement only where all Contracting Jurisdictions have  made such a notification with respect to the existing provision.

Article 9 – Capital Gains from Alienation of Shares or Interests of Entities Deriving their Value  Principally from Immovable Property

Paragraph 1

128.  Paragraph 1 addresses situations in which assets are contributed to an entity shortly before the  sale of shares or comparable interests (such as interests in a partnership or trust) in that entity in order to  dilute the proportion of the value of the entity that is derived from immovable property, based on Article  13(4) of the OECD Model Tax Convention as revised in paragraph 44 (page 72) of the Action 6 Report.  The model provision reads:

4.  Gains derived by a resident of a Contracting State from the alienation of shares or  comparable interests, such as interests in a partnership or trust, may be taxed in the other  Contracting State if, at any time during the 365 days preceding the alienation, these shares  or comparable interests derived more than 50 per cent of their value directly or indirectly  from immovable property, as defined in Article 6, situated in that other State.

129.  The Action 6 Report provides two changes with respect to Article 13(4) of the 2014 version of  the OECD Model Tax Convention: (i) to introduce a testing period for determining whether the condition  on the value threshold is met; and (ii) to expand the scope of interests covered by that paragraph to include  interests comparable to shares, such as interests in a partnership or trust. The provision in paragraph 1 has  been divided into two subparagraphs. Subparagraph a) reflects the introduction of the testing period, and  subparagraph b) reflects the expansion of the interests covered.

130.  In addition, the following changes have been made to the text of the above model provision to  address variations among existing capital gains provisions of Covered Tax Agreements.

(i)  The term “comparable interests” has been replaced with “other rights of participation in an  entity” in the chapeau of this paragraph to make sure that paragraph 1 applies with respect to  existing provisions that may describe the ownership interests more broadly than “comparable  interests”. This change is intended to broadly capture existing provisions to be modified by  this paragraph, but (except to the extent provided in subparagraph b)) not to expand the scope  of the interests covered.

(ii)  The phrase “more than 50 percent” has been replaced with “more than a certain part” to  capture existing provisions using any thresholds, including not only a specified percentage (i.e.  “more than [x] percent” or “at least [x] percent”) but also more general terms such as “the  principal part”, “the greater part”, “mainly”, “wholly”, “principally” and “primarily”.

(iii) The term “real property” has been added to address existing provisions using the term instead  of “immovable property”. In addition, the phrase “as defined in Article 6” has been deleted to  avoid cross-references to a particular article by number.

(iv)  The phrase “more than a certain part of the property of the entity consists of such immovable  property (real property)” has been added to address existing provisions based on Article 13(4)  of the UN Model Tax Convention.

131.  Since the purpose of this provision is to introduce a testing period and to ensure that the provision  addresses interests comparable to shares (such as interest in a partnership or trust), the threshold provided  in existing provisions would be preserved, and where Covered Tax Agreements contain exceptions to the  application of the existing provisions (for example, some Covered Tax Agreements may exclude gains  derived from the alienation of shares of companies that are listed on an approved stock exchange of one of  the Contracting Jurisdictions), those exceptions would continue to apply. Also, some existing provisions  may use the terms “income” and “profits” in addition to or instead of “gains”; such provisions would also  be within the scope of the application of paragraph 1.

Paragraph 2

132.  Paragraph 2 is a compatibility clause which describes the interaction between paragraph 1(a) and  provisions of Covered Tax Agreements. This paragraph clarifies that the 365 day testing period in  paragraph 1(a) replaces the testing periods already contained in existing provisions, or is added where such  testing periods do not exist in existing provisions. If Parties prefer to preserve existing testing periods,  paragraph 6(d) allows the possibility to opt out of paragraph 1(a) with respect to provisions of Covered Tax  Agreements that already include a testing period. Since paragraph 1(b) already describes the relationship  with shares or rights covered by existing provisions, paragraph 2 does not describe the compatibility of  paragraph 1(b) with existing provisions.

Paragraphs 3 and 4

133.  Some Parties may prefer to apply Article 13(4) of the OECD Model Tax Convention, as  produced in the Action 6 Report, to their Covered Tax Agreements, rather than incorporating a testing  period and expanding types of interest covered by existing capital gains provisions. Paragraph 3 allows  such Parties to do so. As noted below in the explanation regarding paragraph 5, paragraph 3 also allows a  Party to introduce a provision addressing gains derived from alienation of shares in entities deriving their  value principally from immovable property (real property) into a Covered Tax Agreement that does not  have such a rule. Paragraph 4 is an optional provision, and, as provided in paragraph 8, will apply to a

Covered Tax Agreement only where all Contracting Jurisdictions have chosen to apply it by making a  notification under paragraph 8. Then, where paragraph 4 applies to a Covered Tax Agreement, paragraph 1  would not apply. In contrast, if one Contracting Jurisdiction chooses to apply paragraph 4 and one or more  of the other Contracting Jurisdictions do not (or neither Contracting Jurisdiction chooses to apply it),  paragraph 4 would not apply to that Covered Tax Agreement, and paragraph 1 would apply.

Paragraph 5

134.  Paragraph 5 is a compatibility clause which describes the interaction between paragraph 4 and  provisions of Covered Tax Agreements. This paragraph clarifies that the provision in paragraph 4 replaces  existing provisions of Covered Tax Agreements addressing capital gains from the alienation of shares or  interests in entities deriving their value principally from immovable property, or is added where such  provisions do not exist in Covered Tax Agreements. If Parties prefer to preserve existing provisions of  their Covered Tax Agreements, paragraph 6(f) allows the possibility to opt out of paragraph 4 with respect  to the Covered Tax Agreements.

135.  The phrase “more than a certain part of the property of the entity consists of such immovable  property (real property)” is intended to ensure that the provision will also modify existing provisions based  on Article 13(4) of the UN Model Tax Convention.

Paragraph 6

136.  Given that a provision addressing capital gains from the alienation of shares or interests in  entities deriving their value principally from immovable property is not required in order to meet a  minimum standard, subparagraph a) allows Parties to opt out of paragraph 1 entirely. In addition,  subparagraphs b) and c) permit Parties to opt out of either paragraph 1(a) or (b) separately.

137.  Subparagraph d) allows Parties to opt out of paragraph 1(a) with respect to their Covered Tax  Agreements that already contain a provision of the type described in paragraph 1 that includes a testing  period.

138.  Subparagraph e) allows Parties to opt out of paragraph 1(b) with respect to their Covered Tax  Agreements that already contain a provision of the type described in paragraph 1 that applies to the  alienation of interests other than shares.

139.  Subparagraph f) allows Parties to opt out of paragraph 4 with respect to their Covered Tax  Agreements that already contain provisions described in paragraph 5. As a result, such existing provisions  would be preserved, and paragraph 4 would apply only with respect to Covered Tax Agreements that do  not contain provisions described in paragraph 5. Since this reservation is intended to work in the situation  where paragraph 4 applies (in other words, paragraph 1 does not apply), it would have no effect on the  application of paragraph 1. On the other hand, Parties that choose to apply paragraph 4 would be able to  make the reservations described in subparagraphs a) through e) in addition to subparagraph f) with respect  to cases where paragraph 1, and not paragraph 4, applies.

Paragraph 7

140.  Paragraph 7 requires each Party (other than a Party that has reserved the right under paragraph  6(a) for paragraph 1 not to apply to all of its Covered Tax Agreements) to notify the Depositary of whether  each of its Covered Tax Agreements contains an existing provision described in paragraph 1, and if so, the  article and paragraph number of each such provision. Given that paragraph 1(a) or (b) could apply even in  the case where the other paragraph is opted out of under the reservations described in paragraph 6(b)  through (e), paragraph 7 does not exclude Parties that have made those reservations from the notification

requirement. Paragraph 1 would apply with respect to a provision of a Covered Tax Agreement only where  all Contracting Jurisdictions have made such a notification with respect to the existing provision.

Paragraph 8

141.  Paragraph 8 requires each Party that chooses to apply paragraph 4 to notify the Depositary of its  choice. A Party that has not reserved the right under paragraph 6(a) for paragraph 1 not to apply to its  Covered Tax Agreements will have included in its notifications under paragraph 7 a list of Covered Tax  Agreements containing a relevant existing provision. A Party that has made such a reservation, however,  will be required to include such a list in its notification under paragraph 8, except where such Party has  reserved the right under paragraph 6(f) to preserve existing provisions. It then describes the relationship  between paragraph 4 and paragraph 1. Where all Contracting Jurisdictions have chosen to apply paragraph  4 by making a notification under this paragraph, paragraph 1 would not apply with respect to that Covered  Tax Agreement, and instead paragraph 4 would apply. An existing provision of a Covered Tax Agreement  would be replaced by the provisions of paragraph 4 where all Contracting Jurisdictions have made a  notification under paragraph 7 or 8 with respect to the existing provision. In other cases, paragraph 4 would  supersede the provisions of the Covered Tax Agreement only to the extent that those provisions are  incompatible with paragraph 4.

Article 10 – Anti-abuse Rule for Permanent Establishments Situated in Third Jurisdictions

Paragraphs 1 through 3

142.  Paragraphs 1 through 3 contain a provision addressing permanent establishments situated in third  jurisdictions, based on the text of the OECD Model Tax Convention produced in paragraph 52 (page 76) of  the Action 6 Report and finalised in the course of follow-up work by WP1. The version of the provision  produced by WP1 as it stood at the time of the development of the Convention reads:

Where

a)  an enterprise of a Contracting State derives income from the other Contracting  State and the first-mentioned State treats such income as attributable to a  permanent establishment of the enterprise situated in a third jurisdiction, and

b)  the profits attributable to that permanent establishment are exempt from tax in  the first-mentioned State,

the benefits of this Convention shall not apply to any item of income on which the tax in the  third jurisdiction is less than the lower of [rate to be determined bilaterally] and 60 per cent  of the tax that would be imposed in the first-mentioned State on that item of income if that  permanent establishment were situated in the first-mentioned State. In such a case any  income to which the provisions of this paragraph apply shall remain taxable according to  the domestic law of the other State, notwithstanding any other provisions of the Convention.

The preceding provisions of this paragraph shall not apply if the income derived from the  other State is derived in connection with or is incidental to the active conduct of a business  carried on through the permanent establishment (other than the business of making,  managing or simply holding investments for the enterprise’s own account, unless these  activities are banking, insurance or securities activities carried on by a bank, insurance  enterprise or registered securities dealer, respectively).

If benefits under this Convention are denied pursuant to the preceding provisions of this  paragraph with respect to an item of income derived by a resident of a Contracting State,  the competent authority of the other Contracting State may, nevertheless, grant these  benefits with respect to that item of income if such competent authority determines that  granting such benefits is justified in light of the reasons such resident did not satisfy the  requirements of this paragraph. The competent authority of the Contracting State to which  a request has been made under the preceding sentence shall consult with the competent  authority of the other Contracting State before either granting or denying the request.

143.  The model provision includes a reference to a tax rate to be determined bilaterally. This relates to  the conditions for denial of benefits of a tax treaty, and provides that the benefits of the treaty will not  apply to any item of income on which the tax rate in the third jurisdiction in which an exempt permanent  establishment is located is less than “the lower of [rate to be determined bilaterally] and 60 percent of the  tax that would be imposed in” the residence jurisdiction of the enterprise. To avoid requiring bilateral  negotiation of a tax rate, the provision in paragraph 1 relies solely on the 60 percent test.

Paragraph 4

144.  Paragraph 4 is a compatibility clause which describes the interaction between paragraphs 1  through 3 and provisions of Covered Tax Agreements. This paragraph provides that the provisions in  paragraphs 1 through 3 replace existing provisions of Covered Tax Agreements that deny or limit benefits  available to an enterprise of a Contracting Jurisdiction which derives income from the other Contracting  Jurisdiction that is attributable to a permanent establishment of the enterprise situated in a third jurisdiction,  or is added where such provisions do not exist in Covered Tax Agreements.

Paragraph 5

145.  Given that a provision addressing permanent establishments situated in third jurisdictions is not  required in order to meet a minimum standard, subparagraph a) allows Parties to opt out of Article 10  entirely. In addition, subparagraph b) allows Parties to opt out of Article 10 entirely with respect to their  Covered Tax Agreements that already contain provisions described in paragraph 4. In contrast,  subparagraph c) allows Parties to opt out of Article 10 entirely with respect to their Covered Tax  Agreements that do not already contain the provisions described in paragraph 4.

Paragraph 6

146.  Paragraph 6 requires each Party (other than a Party that has reserved the right under paragraph  5(a) or (b) for the entirety of Article 10 not to apply to all of its Covered Tax Agreements, or to its Covered  Tax Agreements that already contain a provision of the same type) to notify the Depositary of whether  each of its Covered Tax Agreements contains an existing provision described in paragraph 4, and if so, the  article and paragraph number of each such provision. An existing provision of a Covered Tax Agreement  would be replaced by the provisions of paragraphs 1 through 3 where all Contracting Jurisdictions have  made such a notification with respect to the existing provision. In other cases, paragraphs 1 through 3  would supersede the provisions of the Covered Tax Agreement only to the extent that those provisions are  incompatible with those paragraphs.

Article 11 – Application of Tax Agreements to Restrict a Party’s Right to Tax its Own Residents

Paragraph 1

147.  The provision in paragraph 1 provides a so-called “saving clause” which preserves the right of a  Contracting Jurisdiction to tax its own residents. The provision is based on Article 1(3) of the OECD  Model Tax Convention as set out in paragraph 63 (page 86) of the Action 6 Report, which reads:

3.  This Convention shall not affect the taxation, by a Contracting State, of its residents  except with respect to the benefits granted under paragraph 3 of Article 7, paragraph 2 of

148.  The main changes to the provision in paragraph 1 are to replace references to specific paragraphs  and articles by number with descriptive language based on paragraph 26.19 of the Commentary on Article  1 (Persons covered) of the OECD Model Tax Convention in the Action 6 Report (page 87), which was  developed during the BEPS Project. The references to paragraph 3 of Article 7 (Business profits) and  paragraph 2 of Article 9 (Associated enterprises) in the model provision have been replaced with  subparagraph a), Article 19 (Government service) with subparagraph b), Article 20 (Students) with  subparagraph c), Articles 23A (Exemption method) and 23B (Credit method) with subparagraph d), Article  24 (Non-discrimination) with subparagraph e), Article 25 (Mutual agreement procedure) with  subparagraph f) and Article 28 (Members of diplomatic missions and consular posts) with subparagraph g).

149.  In addition, subparagraphs h) and i) have been included as additional exceptions to the saving  clause, to reflect additional provisions that commonly appear in tax treaties. Subparagraph h) describes  provisions of a Covered Tax Agreement which provide that pensions or other payments made to a resident  of a Contracting Jurisdiction under the social security legislation of the other Contracting Jurisdiction shall  be taxable only in that other Contracting Jurisdiction. This is referred to in paragraph 26.20 of the  Commentary on Article 1 of the OECD Model Tax Convention in the Action 6 Report (page 87) as an  example of provisions that could be included in the list of exceptions. Subparagraph i) covers provisions  that provide for exclusive taxation at source of pensions and similar payments (irrespective of whether or  not they are made under the social security legislation), as well as annuities, alimony payments or other  maintenance payments.

150.  Subparagraph j) is intended to broadly cover provisions that expressly limit taxation rights of the  residence jurisdiction or expressly allow taxation rights exclusively to the source jurisdiction. That  subparagraph would also cover provisions that provide for exemption of income in both jurisdictions (for  example, in the case of child support payments under some existing treaties). It would also cover, for  example, the following types of provisions:

•  provisions which allow the competent authority of a Contracting Jurisdiction that has made or is  to make an initial adjustment to the profits of an enterprise of that Contracting Jurisdiction to  provide relief from double taxation;

•  provisions which require a Contracting Jurisdiction to consider the acquisition value of a property  owned by its resident to be its fair market value at the time when he ceases to be a resident of the  other Contracting Jurisdiction and becomes a resident of the first-mentioned Contracting  Jurisdiction; or

•  provisions which grant deductions for contributions made by a resident of a Contracting  Jurisdiction to a retirement plan in the other Contracting Jurisdiction in computing income in the  first-mentioned Contracting Jurisdiction.

151.  Given the variations of existing provisions of Covered Tax Agreements, the following additional  changes have been made to the language of paragraph 1.

(i)  With respect to the phrase “Contracting Jurisdiction, or a political subdivision or local  authority” in the description of the Commentary corresponding to subparagraph b), some  Covered Tax Agreements may use other formulations, including “State power or  administrative authority”, “regional authority”, “public body”, “public entities”, “statutory  body”, “political or administrative subdivision”, “administrative-territorial subdivision/unit”,  “Land”, “legal person organised under public law” or “legal entity under public law”. To  cover these variations, the more general term “other comparable body” has been added in that  subparagraph.

(ii)  While Article 20 of the OECD Model Tax Convention addresses taxation of a “student”, some  existing provisions of Covered Tax Agreements may cover a “business apprentice” or “trainee”  in addition to a student. Also, some Covered Tax Agreements may contain the provisions  concerning taxation of a “teacher”, “professor”, “lecturer”, “instructor”, “researcher” or  “research scholar”. These terms have been added in subparagraph c) to ensure that these types  of provisions are covered.

(iii)  The phrase “relief of double taxation” in the description of the Commentary corresponding to  subparagraph d) has been replaced with “tax credit or tax exemption” to ensure that provisions  applying the credit method or exemption method would continue to apply as intended even  where a Covered Tax Agreement provides for tax sparing.

(iv)  The term “government mission” has been added to subparagraph g) to reflect certain Covered  Tax Agreements concluded by non-state jurisdictions.

Paragraph 2

152.  Paragraph 2 is a compatibility clause which describes the interaction between paragraph 1 and  provisions of Covered Tax Agreements. This paragraph clarifies that the provision in paragraph 1 replaces  existing provisions of Covered Tax Agreements stating that the Covered Tax Agreements would not affect  the taxation by a Contracting Jurisdiction of its residents, or is added where such provisions do not exist in  Covered Tax Agreements.

Paragraph 3

153.  Given that a saving clause is not required in order to meet a minimum standard, subparagraph a)  allows Parties to opt out of Article 11 entirely. In addition, recognising that where Covered Tax  Agreements include a saving clause provision, it is usually customised based on the content of the Covered  Tax Agreements, subparagraph b) allows the Parties to opt out of Article 11 entirely with respect to  Covered Tax Agreements that already contain a saving clause.

154.  Paragraph 26.16 of the Commentary on Article 1 of the OECD Model Tax Convention in the  Action 2 Report (page 143) notes that a saving clause would supplement the fiscally transparent entities  provision. Therefore, it is expected that a Party that adopts the provision on transparent entities contained  in Article 3(1) would also adopt a provision ensuring that its application will not interfere with the taxation  by a Contracting Jurisdiction of its residents, such as the saving clause provided in Article 11. Recognising,  however, that some Parties may prefer a more targeted solution, subparagraph a) allows Parties to opt out  of Article 11. In such a case, Article 3(3) applies to introduce a saving clause that relates solely to the  provision in Article 3(1).

Paragraph 4

155.  Paragraph 4 requires each Party (other than a Party that has reserved the right under paragraph  3(a) or (b) for the entirety of Article 11 not to apply to all of its Covered Tax Agreements, or to its Covered  Tax Agreements that already contain a provision of the same type) to notify the Depositary of whether  each of its Covered Tax Agreements contains an existing saving clause, and if so, the article and paragraph  number of each such provision. An existing provision of a Covered Tax Agreement would be replaced by  the provisions of paragraph 1 where all Contracting Jurisdictions have made such a notification with  respect to the existing provision. In other cases, paragraph 1 would supersede the provisions of the  Covered Tax Agreement only to the extent that those provisions are incompatible with paragraph 1.

Part IV. Avoidance of Permanent Establishment Status

156.  The work on Action 7 led to changes to the definition of permanent establishment to prevent the  artificial avoidance of permanent establishment status in relation to BEPS, including through the use of  commissionnaire arrangements and the specific activity exemptions. Part IV of the Convention contains 4  Articles arising from the work on Action 7. These Articles seek to amend existing tax treaties to counter  the artificial avoidance of permanent establishment status through: (i) commissionnaire arrangements and  similar strategies (Article 12 of the Convention); (ii) the specific activity exemptions (Article 13 of the  Convention); and (iii) the splitting-up of contracts (Article 14 of the Convention). Article 15 of the  Convention provides the definition of the term “closely related to an enterprise,” which is used in Articles  12 through 14.

Article 12 - Artificial Avoidance of Permanent Establishment Status through Commissionnaire  Arrangements and Similar Strategies

157.  The work on Action 7 led to changes to the wording of Article 5(5) and (6) of the 2014 version of  the OECD Model Tax Convention to address the artificial avoidance of permanent establishment status  through commissionnaire arrangements and similar strategies. Article 12 of the Convention, which consists  of 6 paragraphs, sets out the interaction between incorporating this aspect of the work on Action 7 and  Covered Tax Agreements.

Paragraph 1

158.  Paragraph 1 is based on the text of Article 5(5) of the OECD Model Tax Convention produced on  page 16 of the Action 7 Report (Preventing the Artificial Avoidance of Permanent Establishment Status),  which reads as follows:

5.  Notwithstanding the provisions of paragraphs 1 and 2 but subject to the provisions of  paragraph 6, where a person is acting in a Contracting State on behalf of an enterprise and,  in doing so, habitually concludes contracts, or habitually plays the principal role leading to  the conclusion of contracts that are routinely concluded without material modification by  the enterprise, and these contracts are

a)  in the name of the enterprise, or

b)  for the transfer of the ownership of, or for the granting of the right to use,  property owned by that enterprise or that the enterprise has the right to use, or

c)  for the provision of services by that enterprise,

that enterprise shall be deemed to have a permanent establishment in that State in respect of  any activities which that person undertakes for the enterprise, unless the activities of such  person are limited to those mentioned in paragraph 4 which, if exercised through a fixed  place of business, would not make this fixed place of business a permanent establishment  under the provisions of that paragraph.

159.  The provision in paragraph 1 reflects changes to the model text of Article 5(5) to conform the  terminology used therein to the terminology used in the Convention, and to replace cross-references to  paragraphs of the OECD Model Tax Convention with a description of those provisions. Furthermore, given  that the Action 7 work has also resulted in modifications to Article 5(4) and (6) of the 2014 version of the  OECD Model Tax Convention, changes are also made to the model text of Article 5(5) to take into account  that the equivalent of Article 5(4) and (6) of Covered Tax Agreements might have been modified by the  provisions of the Convention.

Paragraph 2

160.  Paragraph 2 is based on Article 5(6)(a) of the OECD Model Tax Convention produced on page  16 of the Action 7 Report, which reads as follows:

Paragraph 5 shall not apply where the person acting in a Contracting State on behalf of an  enterprise of the other Contracting State carries on business in the first-mentioned State as  an independent agent and acts for the enterprise in the ordinary course of that business.  Where, however, a person acts exclusively or almost exclusively on behalf of one or more  enterprises to which it is closely related, that person shall not be considered to be an  independent agent within the meaning of this paragraph with respect to any such enterprise.

161.  Changes are made in paragraph 2 to the text of Article 5(6)(a) of the OECD Model Tax  Convention to conform the terminology used therein to the terminology used in the Convention and to  replace the reference to Article 5(5) of the OECD Model Tax Convention with a reference to Article 12(1)  of the Convention.

Paragraph 3

162.  Paragraph 3 is a compatibility clause which describes the interaction between paragraphs 1 and 2  and provisions of Covered Tax Agreements. Existing tax treaties may include a wide variety of such  provisions. Although many will be modelled after Article 5(5) of the 2014 version of the OECD Model  Tax Convention, existing tax treaties frequently contain variations based on Article 5(5)(b) of the 2011  version of the UN Model Tax Convention or provisions that have been bilaterally customised.

163.  Paragraph 3(a) provides that paragraph 1 would replace provisions of a Covered Tax Agreement  to the extent that the provisions describe the conditions under which an enterprise shall be deemed to have  a dependent agent permanent establishment, but only to the extent that such variations address the situation  in which a person has, and habitually exercises, an authority to conclude contracts in the name of an  enterprise. The reference to contracts “in the name of” is intended to cover other common variations of  language, including “on behalf of”, “that are binding on” or other variations that are commonly used.

164.  Paragraph 3(b) provides that paragraph 2 would replace provisions of a Covered Tax Agreement  that provide that an enterprise shall not be deemed to have a permanent establishment in a Contracting  Jurisdiction in respect of an activity which an agent of an independent status undertakes for the enterprise.  Such provisions of a Covered Tax Agreement would include those modelled after, for example, Article 5(6)  of the 2014 version of the OECD Model Tax Convention or Article 5(7) of the 2011 version of the UN  Model Tax Convention, as well as bilaterally negotiated provisions of the same type.

Paragraph 4

165.  Given that provisions addressing artificial avoidance of permanent establishment status through  commissionnaire arrangements and similar strategies are not required in order to meet a minimum standard,  paragraph 4 allows a Party to reserve the right not to apply the entirety of Article 12 to its Covered Tax  Agreements.

Paragraph 5

166.  Paragraph 5 requires each Party (other than a Party that has opted out of the entirety of Article 12)  to notify the Depositary of each of its Covered Tax Agreements that contains an existing provision of the  same type as the provision in paragraph 1, and the article and paragraph number of each such provision.  Paragraph 1 would apply with respect to a provision of a Covered Tax Agreement only where all  Contracting Jurisdictions to the Covered Tax Agreement have made such a notification.

Paragraph 6

167.  Paragraph 6 requires each Party (other than a Party that has opted out of the entirety of Article 12)  to notify the Depositary of each of its Covered Tax Agreements that contains an existing provision of the  same type as the provision in paragraph 2, and the article and paragraph number of each such provision.  Paragraph 2 would apply with respect to a provision of a Covered Tax Agreement only where all  Contracting Jurisdictions to the Covered Tax Agreement have made such a notification.

Article 13 - Artificial Avoidance of Permanent Establishment Status through the Specific Activity  Exemptions

168.

Paragraph 1

169.  The work on Action 7 led to changes in the text of Article 5(4) of the OECD Model Tax  Convention as shown in pages 28 and 29 of the Action 7 Report, to explicitly state that the activities listed  therein will be deemed not to constitute a permanent establishment only if they are of a preparatory or  auxiliary character. Paragraph 30.1 of the Commentary on Article 5 (see page 38 of the Action 7 Report)  notes, however, that some States consider that some of the activities referred to in Article 5(4) of the 2014  version of the OECD Model Tax Convention are intrinsically preparatory or auxiliary and, in order to  provide greater certainty for both tax administrations and taxpayers, take the view that these activities  should not be subject to the condition that they be of a preparatory or auxiliary character, and that concern  about inappropriate use of the specific activity exemptions can be addressed through anti-fragmentation  rules. An alternative provision reflecting this view was therefore included in paragraph 30.1. Article 5(4),  as produced on pages 28 and 29 of the Action 7 Report, is reflected in Article 13(2) (Option A) and the

provision contained in paragraph 30.1 of the Commentary on Article 5 is reflected in Article 13(3) (Option  B). Article 13(1) provides that a Party may choose to apply Option A or Option B or not to apply either of  these options.

Paragraph 2 – Option A

170.  Option A is based on the principles reflected in the text of Article 5(4) of the OECD Model Tax  Convention produced on pages 28 and 29 of the Action 7 Report to address concerns of artificial avoidance  of permanent establishment status through the specific activity exemptions. The model text of Article 5(4)  reads:

4.  Notwithstanding the preceding provisions of this Article, the term “permanent  establishment” shall be deemed not to include:

a)  the use of facilities solely for the purpose of storage, display or delivery of  goods or merchandise belonging to the enterprise;

b)  the maintenance of a stock of goods or merchandise belonging to the enterprise  solely for the purpose of storage, display or delivery;

c)  the maintenance of a stock of goods or merchandise belonging to the enterprise  solely for the purpose of processing by another enterprise;

d)  the maintenance of a fixed place of business solely for the purpose of  purchasing goods or merchandise or of collecting information, for the  enterprise;

e)  the maintenance of a fixed place of business solely for the purpose of carrying  on, for the enterprise, any other activity;

f)  the maintenance of a fixed place of business solely for any combination of  activities mentioned in subparagraphs a) to e),

provided that such activity or, in the case of subparagraph f), the overall activity of the fixed  place of business, is of a preparatory or auxiliary character.

171.  Recognising that the specific activity exemptions listed in existing tax treaties frequently contain  activities which vary from the model text of Article 5(4) (including variations based on Article 5(4) of the  2011 version of the UN Model Tax Convention and in some instances, bilaterally negotiated qualifying  activities), Article 13(2) of the Convention is drafted to apply the principles contained in the model text of

establishment status, or the position that they are already contingent on the activity being of a preparatory  or auxiliary character.

Paragraph 3 – Option B

172.  Option B is based on the provision contained in paragraph 30.1 of the Commentary on Article 5  (see page 38 of the Action 7 Report) which reads:

4.  Notwithstanding the preceding provisions of this Article, the term “permanent  establishment” shall be deemed not to include:

a)  the use of facilities solely for the purpose of storage, display or delivery of  goods or merchandise belonging to the enterprise;

b)  the maintenance of a stock of goods or merchandise belonging to the enterprise  solely for the purpose of storage, display or delivery;

c)  the maintenance of a stock of goods or merchandise belonging to the enterprise  solely for the purpose of processing by another enterprise;

d)  the maintenance of a fixed place of business solely for the purpose of  purchasing goods or merchandise or of collecting information, for the  enterprise;

e)  the maintenance of a fixed place of business solely for the purpose of carrying  on, for the enterprise, any activity not listed in subparagraphs a) to d), provided  that this activity has a preparatory or auxiliary character, or

f)  the maintenance of a fixed place of business solely for any combination of  activities mentioned in subparagraphs a) to e), provided that the overall activity  of the fixed place of business resulting from this combination is of a  preparatory or auxiliary character.

173.  As in the case of Option A, the text in Option B has been revised to take into account the fact that  the specific activity exemptions listed in Covered Tax Agreements could vary from the provision contained  in paragraph 30.1 of the Commentary on Article 5. That is, in the case of a Covered Tax Agreement with  text identical to that of Article 5 of the 2014 version of the OECD Model Tax Convention or the 2011  version of the UN Model Tax Convention, Article 13(3)(a) would correspond to Article 5(4)(a) through (d)  of the Covered Tax Agreement. Article 13(3)(b) and Article 13(3)(c) of the Convention would correspond  to Article 5(4)(e) and (f) of the Covered Tax Agreement, respectively. The effect of applying Article 13(3)  of the Convention would be to preserve the exceptions for activities described in Article 5(4)(a) through (d)  of the Covered Tax Agreement, but to ensure that those exceptions will apply irrespective of whether the  activity is of a preparatory or auxiliary character. This would be true whether that Contracting Jurisdiction  takes the position that the exceptions in Article 5(4)(a) through (d) of that Covered Tax Agreement are  considered per se exceptions to permanent establishment status, or the position that they are already  contingent on the activity being of a preparatory or auxiliary character. An exception is provided in Article  13(3)(a) of the Convention, however, in order to preserve existing provisions of a Covered Tax Agreement  that explicitly provide that a specific activity shall be deemed not to constitute a permanent establishment  provided that the activity is of a preparatory or auxiliary character.

Paragraph 4

174.  Paragraph 4 is based on the text of the new Article 5(4.1) of the OECD Model Tax Convention  produced in page 39 of the Action 7 Report to address the fragmentation of activities between closely  related parties. Paragraph 4.1 reads:

4.1  Paragraph 4 shall not apply to a fixed place of business that is used or maintained by  an enterprise if the same enterprise or a closely related enterprise carries on business  activities at the same place or at another place in the same Contracting State and

a)  that place or other place constitutes a permanent establishment for the  enterprise or the closely related enterprise under the provisions of this Article,  or

b)  the overall activity resulting from the combination of the activities carried on by  the two enterprises at the same place, or by the same enterprise or closely  related enterprises at the two places, is not of a preparatory or auxiliary  character,

provided that the business activities carried on by the two enterprises at the same place, or  by the same enterprise or closely related enterprises at the two places, constitute  complementary functions that are part of a cohesive business operation.

175.   Changes are made to the model text of Article 5(4.1) in Article 13(4) to conform the terminology  used therein to the terminology used in the Convention. In addition, the reference to Article 5(4) of the  OECD Model Tax Convention has been replaced with a description of that provision instead (as it may be  modified by Article 13(2) or (3)).

Paragraph 5

176.  Paragraph 5 contains compatibility clauses which describe the relationship between Article 13(2)  through (4) and provisions of Covered Tax Agreements.

177.  Paragraph 5(a) provides that Article 13(2) or (3) shall apply in place of the relevant parts of  provisions of a Covered Tax Agreement that describe a list of specific activities deemed not to constitute a  permanent establishment even if the activity is carried on through a fixed place of business. Such  provisions of a Covered Tax Agreement would include, for example, those modelled after Article 5(4) of  the 2014 version of the OECD Model Tax Convention or of the 2011 version of the UN Model Tax  Convention, as well as bilaterally negotiated provisions of the same type. The phrase “provisions of a  Covered Tax Agreement that operate in a comparable manner” contained in paragraph 5(a) and (b), would  include, for example, provisions of a Covered Tax Agreement that describe specific activities which are  deemed not to constitute a permanent establishment in a single sentence, rather than by listing those  activities, but would not include, for example, specific provisions that provide that a project or activity  constitutes a permanent establishment only if a time period test is met.

178.  Paragraph 5(b) provides that Article 13(4) shall apply to provisions of a Covered Tax Agreement  (as they may be modified by paragraph 2 or 3) that describe a list of specific activities deemed not to  constitute a permanent establishment even if the activity is carried on through a fixed place of business.  Such provisions of a Covered Tax Agreement would include those modelled after, for example, Article 5(4)  of the 2014 version of the OECD Model Tax Convention or of the 2011 version of the UN Model Tax  Convention, as well as bilaterally negotiated provisions of the same type.

Paragraph 6

179.   Given that the provisions addressing artificial avoidance of permanent establishment status  through the specific activity exemptions and fragmentation of activities between closely related parties are  not required in order to meet a minimum standard, a Party may reserve the right for the entirety of Article  13 not to apply to its Covered Tax Agreements. A Party that chooses to apply Option A under Article 13(1)  may also reserve the right for Article 13(2) (Option A) not to apply to provisions of a Covered Tax  Agreement that already explicitly state that the activities listed therein shall be deemed not to constitute a  permanent establishment only if they are of a preparatory or auxiliary character. Finally, a Party may  reserve the right not to apply Article 13(4).

Paragraph 7

180.   Paragraph 7 requires that Parties that opted for Option A (Article 13(2)) or Option B (Article  13(3)) shall notify the Depositary of their choice of Option. That notification would also include a list of  each of its Covered Tax Agreements that includes specific activity exemptions, including those that are  subject to a reservation under paragraph 6(b), as well as the article and paragraph number of each such  provision. An Option would apply to a provision only where all Contracting Jurisdictions have chosen to  apply the same Option and have made such a notification with respect to that provision.

Paragraph 8

181.  Paragraph 8 requires each Party that has not opted out of applying paragraph 4 (or the entirety of

Article 14 – Splitting-up of Contracts

182.  The Action 7 Report noted that the splitting-up of contracts is a potential strategy for the artificial  avoidance of permanent establishment status through abuse of the exception in Article 5(3) of the OECD  Model Tax Convention. The Action 7 Report further noted that the PPT provision will address such BEPS  concerns related to the abusive splitting-up of contracts. The Action 7 Report includes a draft provision  specifically addressing the splitting-up of contracts for use in treaties that would not include the PPT, or for  Contracting Jurisdictions that wish to address such abuses explicitly. Article 14 of the Convention provides  for the implementation of that provision.

Paragraph 1

183.  Paragraph 1 is based on the text in revised paragraph 18.1 of the Commentary on Article 5 which  is produced on page 43 of the Action 7 Report as amended in the course of the follow-up work carried out  by WP1. The version of the provision produced by WP1 as it stood at the time of the development of the  Convention reads as follows:

For the sole purpose of determining whether the twelve month period referred to in  paragraph 3 has been exceeded,

a)  where an enterprise of a Contracting State carries on activities in the other  Contracting State at a place that constitutes a building site or construction or  installation project and these activities are carried on during one or more  periods of time that, in the aggregate, exceed 30 days without exceeding twelve  months, and

b)  connected activities are carried on at the same building site or construction or  installation project during different periods of time, each exceeding 30 days, by  one or more enterprises closely related to the first-mentioned enterprise,

these different periods of time shall be added to the aggregate period of time during which  the first-mentioned enterprise has carried on activities at that building site or construction  or installation project.

184.  Changes have been made to the text above to conform the terminology used therein to the  terminology used in the Convention. In addition, consistent with other provisions of the Convention, the  reference to “the twelve month period referred to in paragraph 3 [of Article 5 of the OECD Model Tax  Convention]” has been replaced with a description of that provision instead. Furthermore, given that the  descriptions of activities and places covered by existing provisions may differ from those covered by the  OECD Model Tax Convention (for example, because they are modelled after Article 5(3)(a) of the 2011  version of the UN Model Tax Convention or reflect bilateral negotiation), Article 14(1)(a) and (b) of the  Convention have been drafted to reflect these existing variations.

Paragraph 2

185.  Paragraph 2 is the compatibility clause which describes the relationship between Article 14(1) of  the Convention and provisions of Covered Tax Agreements. The compatibility clause provides that the  splitting-up of contracts rule shall apply in place of or in the absence of provisions in Covered Tax  Agreements to the extent that such provisions address the division of contracts into multiple parts to avoid  the application of a time period in relation to the existence of a permanent establishment for specific  projects or activities. Many treaties feature anti-splitting rules that apply to a wide variety of activities,  only some of which may be covered by the provision in Article 14. Paragraph 2 is intended to replace those  existing rules only to the extent that they relate to the activities described in paragraph 1, and to leave those  rules intact with respect to activities that are not within the scope of paragraph 1. This would be the case,  for example, where the same anti-splitting rule is used for a provision relating to construction activities  carried on through a fixed place of business and for a provision deeming a permanent establishment to  exist in the case of provision of services that are not tied to a specific place of business.

Paragraph 3

186.  Given that the provisions addressing artificial avoidance of permanent establishment status  through splitting-up of contracts are not required in order to meet a minimum standard, paragraph 3(a)  permits a Party to reserve the right for the entirety of Article 14 not to apply with respect to its Covered  Tax Agreements. Furthermore, recognising that a Covered Tax Agreement could contain anti-contract  splitting rules that are specifically addressed to the exploration for or exploitation of natural resources, and  that these provisions are frequently carefully negotiated, paragraph 3(b) allows a Party to reserve on the  application of Article 14(1) only with respect to the existence of a permanent establishment relating to the  exploration for or exploitation of natural resources.

Paragraph 4

187.  Paragraph 4 requires each Party (other than a Party that has opted out of the entirety of the Article)  to notify the Depositary of whether each of its Covered Tax Agreements contains an existing anti-contract  splitting provision that is not subject to a reservation under paragraph 3(b), and if so, the article and  paragraph number of each such provision. Paragraph 1 will replace such provisions to the extent provided  in paragraph 2 where all Contracting Jurisdictions to the Covered Tax Agreement have made such a  notification. In other cases, paragraph 1 will apply to the Covered Tax Agreement, but will supersede the  existing provisions of the Covered Tax Agreement only to the extent that those provisions are incompatible  with paragraph 1.

Article 15 – Definition of a Person Closely Related to an Enterprise

Paragraph 1

188.  Paragraph 1 describes the conditions under which a person will be considered to be “closely  related” to an enterprise for the purposes of Articles 12, 13 and 14. The definition is based on the text of

b)  For the purposes of this Article, a person is closely related to an enterprise if, based  on all the relevant facts and circumstances, one has control of the other or both are  under the control of the same persons or enterprises. In any case, a person shall be  considered to be closely related to an enterprise if one possesses directly or indirectly  more than 50 per cent of the beneficial interest in the other (or, in the case of a  company, more than 50 per cent of the aggregate vote and value of the company’s  shares or of the beneficial equity interest in the company) or if another person  possesses directly or indirectly more than 50 per cent of the beneficial interest (or, in  the case of a company, more than 50 per cent of the aggregate vote and value of the  company’s shares or of the beneficial equity interest in the company) in the person  and the enterprise.

189.  To reflect the structure of the Convention, the reference to “this Article” has been replaced with  references to the provisions of the Covered Tax Agreement that have been modified by Articles 12, 13 and  14 of the Convention, to ensure that it applies only to provisions of the Covered Tax Agreement that have  been modified by those Articles to include the concept of a “closely related” enterprise.

Paragraph 2

190.   Given that Article 15(1) is intended to apply to provisions of a Covered Tax Agreement that  have been modified by a provision of the Convention that uses the term “closely related to an enterprise”  (specifically Article 12(2), Article 13(4), and Article 14(1) of the Convention), Parties can opt out of

Part V. Improving Dispute Resolution

191.  The Action 14 Report contains a commitment by the jurisdictions engaged in the work to  implement a minimum standard for improving dispute resolution (“the Action 14 minimum standard”).  The Action 14 minimum standard is complemented by a set of best practices, and some elements of the  Action 14 minimum standard can be satisfied and some best practices can be implemented by  incorporating specific provisions into tax treaties. Part V of the Convention provides ways to incorporate  these provisions into Covered Tax Agreements.

Article 16 – Mutual Agreement Procedure

192.   Element 1.1 of the Action 14 minimum standard requires jurisdictions to include Article 25(1)  through (3) of the OECD Model Tax Convention in their tax treaties, as interpreted in the Commentary to  the OECD Model Tax Convention and subject to the variations in these paragraphs provided for under  elements 3.1 and 3.3 of the Action 14 minimum standard. Article 16 would allow Parties to modify their  Covered Tax Agreements, to incorporate the contents of Article 25(1) through (3) of the OECD Model Tax  Convention.

Paragraphs 1 through 3

193.

1.  Where a person considers that the actions of one or both of the Contracting States  result or will result for him in taxation not in accordance with the provisions of this  Convention, he may, irrespective of the remedies provided by the domestic law of those  States, present his case to the competent authority of either Contracting State. The case  must be presented within three years from the first notification of the action resulting in  taxation not in accordance with the provisions of the Convention.

2.  The competent authority shall endeavour, if the objection appears to it to be justified  and if it is not itself able to arrive at a satisfactory solution, to resolve the case by mutual  agreement with the competent authority of the other Contracting State, with a view to the  avoidance of taxation which is not in accordance with the Convention. Any agreement  reached shall be implemented notwithstanding any time limits in the domestic law of the  Contracting States.

3.  The competent authorities of the Contracting States shall endeavour to resolve by  mutual agreement any difficulties or doubts arising as to the interpretation or application of  the Convention. They may also consult together for the elimination of double taxation in  cases not provided for in the Convention.

194.  Changes have been made to the text of the model provisions to conform the terminology used  therein to the terminology used in the Convention.

Paragraph 4

195.  Paragraph 4 is a compatibility clause which describes the interaction between Article 16(1)  through (3) and the provisions of Covered Tax Agreements. In general, these compatibility clauses reflect

that members of the ad hoc Group preferred to retain existing provisions relating to dispute resolution to  the extent that those provisions are consistent in content with the provisions of paragraphs 1, 2 and 3 (and  subject to any reservations provided in paragraph 5). As with other Articles, minor variations in language  will not prevent a provision from falling within the scope of the compatibility clauses in paragraph 4.

196.  Paragraph 4(a) contains 2 clauses which set out the interaction between Article 16(1) and  provisions of Covered Tax Agreements as follows:

(i)  Paragraph 4(a)(i) provides that the first sentence of Article 16(1) of the Convention would  replace provisions of a Covered Tax Agreement that provide that where a person considers  that the actions of one or both of the Contracting Jurisdictions result or will result for that  person in taxation not in accordance with the provisions of the Covered Tax Agreement, that  person may, irrespective of the remedies provided by the domestic law of those Contracting  Jurisdictions, present the case to the competent authority of the Contracting Jurisdiction of  which that person is a resident, including provisions under which, if the case presented by that  person comes under the Article of the Covered Tax Agreement relating to non-discrimination  based on nationality, the case may be presented to the competent authority of the Contracting  Jurisdiction of which that person is a national. Such provisions of a Covered Tax Agreement  would include those modelled after, for example, the first sentence of Article 25(1) of the  2014 version of the OECD Model Tax Convention or of the 2011 version of the UN Model  Tax Convention. Paragraph 4(a)(i) would also apply in the absence of such a provision in a  tax treaty.

(ii)  Paragraph 4(a)(ii) provides that the second sentence of Article 16(1) of the Convention would  replace provisions of a Covered Tax Agreement that provide that the mutual agreement  procedure case must be presented within a specific time period that is shorter than three years  from the first notification of the action resulting in taxation not in accordance with the  provisions of a Covered Tax Agreement. This would preserve longer time periods provided in  Covered Tax Agreements without necessitating a reservation not to apply the second sentence  of Article 25(1) to these Covered Tax Agreements. Paragraph 4(a)(ii) would also add the  second sentence of Article 16(1) to Covered Tax Agreements in the absence of a provision  describing a time period within which a case must be presented.

197.  Paragraph 4(b) contains 2 subparagraphs which set out the interaction between Article 16(2) and  provisions of Covered Tax Agreements as follows:

(i)  Paragraph 4(b)(i) provides that the first sentence of Article 16(2) would apply to Covered Tax  Agreements that do not contain a provision that provides that the competent authority that is  presented with the case by the person referred to in Article 16(1) shall endeavour, if the  objection appears to it to be justified and if it is not itself able to arrive at a satisfactory  solution, to resolve the case by mutual agreement with the competent authority of the other  Contracting Jurisdiction, with a view to the avoidance of taxation which is not in accordance  with the Covered Tax Agreement. Such provisions of a Covered Tax Agreement would  include, for example, those modelled after the first sentence of Article 25(2) of the OECD  Model Tax Convention or of the UN Model Tax Convention.

(ii)  Paragraph 4(b)(ii) provides that the second sentence of Article 16(2) would apply to Covered  Tax Agreements that do not contain a provision that provides that any agreement reached via  the mutual agreement procedure shall be implemented notwithstanding any time limits in the  domestic law of the Contracting Jurisdictions. Such provisions of a Covered Tax Agreement  would include, for example, those modelled after the second sentence of Article 25(2) of the

2014 version of the OECD Model Tax Convention or of the 2011 version of the UN Model  Tax Convention.

198.   Paragraph 4(c) contains 2 subparagraphs which set out the interaction between Article 16(3) and  provisions of Covered Tax Agreements as follows:

(i)  Paragraph 4(c)(i) provides that the first sentence of Article 16(3) would apply to Covered Tax  Agreements that do not contain a provision that provides that the competent authorities of the  Contracting Jurisdictions shall endeavour to resolve by mutual agreement any difficulties or  doubts arising as to the interpretation or application of the Covered Tax Agreement. Such  provisions of a Covered Tax Agreement would include, for example, those modelled after the  first sentence of Article 25(3) of the 2014 version of the OECD Model Tax Convention or of  the 2011 version of the UN Model Tax Convention.

(ii)  Paragraph 4(c)(ii) provides that the second sentence of Article 16(3) would apply to Covered  Tax Agreements that do not contain a provision which provides that the competent authorities  of the Contracting Jurisdictions may also consult together for the elimination of double  taxation in cases not provided for in the tax treaty. Such provisions of a Covered Tax  Agreement would include, for example, those modelled after the second sentence of Article  25(3) of the OECD Model Tax Convention or of the UN Model Tax Convention.

Paragraph 5

199.  As explained above, element 1.1 of the Action 14 minimum standard requires jurisdictions to  include Article 25(1) through (3) of the OECD Model Tax Convention in their tax treaties, subject to the  variations in these paragraphs provided for under elements 3.1 and 3.3 of the Action 14 minimum standard.  In this regard, while Article 16(1) through (3) would effectively incorporate Article 25(1) through (3) of  the OECD Model Tax Convention into Covered Tax Agreements, Article 16(5) recognises that Parties are  also permitted to implement element 1.1 of the Action 14 minimum standard through administrative  measures, as provided under elements 3.1 and 3.3 of the Action 14 minimum standard. Article 16(5)  provides reservations from Article 16(1) and (2) to reflect these variations.

200.

3.1  Both competent authorities should be made aware of MAP requests being submitted  and should be able to give their views on whether the request is accepted or rejected. In  order to achieve this, countries should either:

•  amend paragraph 1 of Article 25 to permit a request for MAP assistance to be  made to the competent authority of either Contracting State, or

•  where a treaty does not permit a MAP request to be made to either Contracting  State, implement a bilateral notification or consultation process for cases in  which the competent authority to which the MAP case was presented does not  consider the taxpayer’s objection to be justified (such consultation shall not be  interpreted as consultation as to how to resolve the case).

201.  As explained above, the second sentence of Article 16(1) of the Convention would replace  provisions of a Covered Tax Agreement that provide that a mutual agreement procedure case must be  presented within a specific time period that is shorter than three years from the first notification of the  action resulting in taxation not in accordance with the provisions of the Covered Tax Agreement or would  apply in the absence of specific time period provided in the tax treaty. Recognising that Contracting  Jurisdictions are left free to agree in their tax treaties to omit the second sentence of Article 25(1) of the  OECD Model Tax Convention if their respective domestic regulations apply automatically and are more  favourable in their effects to the taxpayer, either because they allow a longer time for presenting objections  or because they do not set any time limits for such purpose, Article 16(5)(b) allows a Party to reserve on  the application of the second sentence of Article 16(1) in instances where its tax treaty does not contain a  provision stipulating the time period for the taxpayer to present the case for competent authority discussion  under the mutual agreement procedure. A Party may make such a reservation only if it intends to ensure  that even in the absence of such a provision, a taxpayer would be permitted to present its case within a  period of at least three years from the first notification of the action resulting in taxation not in accordance  with the provisions of the Covered Tax Agreement. It is anticipated, therefore, that this reservation would  only be made by a Contracting Jurisdiction to a Covered Tax Agreement if its domestic regulations apply  automatically and are more favourable in their effects to the taxpayer, either because they allow a longer  time for presenting objections or because they do not set any time limits for such purpose.

202.

3.3  Countries should include in their tax treaties the second sentence of paragraph 2 of

It is understood that where one Contracting Jurisdiction to a Covered Tax Agreement prefers to include the  second sentence of Article 16(2) and the other Contracting Jurisdiction opts out of its application, whether  such an alternative provision would be added to the Covered Tax Agreement would be a matter for  bilateral negotiations.

Paragraph 6

203.  Paragraph 6 requires a number of notifications, to ensure clarity as to how Covered Tax  Agreements will be modified by Article 16. Paragraph 6(a) requires each Party (other than a Party that has  reserved the right not to apply the first sentence of paragraph 1) to notify the Depositary of whether each of  its Covered Tax Agreements contains an existing provision that provides that a taxpayer may present its  case to the competent authority of the Contracting Jurisdiction of which that person is a resident (or a  national, if the issue involves non-discrimination based on nationality), and if so, the article and paragraph  number of each such provision. When all Contracting Jurisdictions to a Covered Tax Agreement have  made a notification with respect to a provision of a Covered Tax Agreement, the first sentence of  paragraph 1 replaces that provision. In other cases (except where one of the Contracting States has reserved  the right not to apply the first sentence of paragraph 1), the first sentence of paragraph 1 shall apply to the  Covered Tax Agreement, but shall supersede the existing provision of the Covered Tax Agreement only to  the extent that those provisions are incompatible with that sentence.

204.   Paragraph 6(b)(i) requires each Party that has not reserved the right not to apply the second  sentence of paragraph 1 to notify the Depositary of the list of its Covered Tax Agreements which provide  that a case referred to in the first sentence of Article 16(1) must be presented within a specific time period  that is shorter than three years from the first notification of the action resulting in taxation not in  accordance with the provisions of the Covered Tax Agreement, as well as the Article and paragraph  number of each such provision. Paragraph 6(b)(ii) requires each Party that has not reserved the right not to  apply the second sentence of paragraph 1 to notify the Depositary of the list of its Covered Tax  Agreements (as well as the article and paragraph number of each such provision) which include a provision  that provides that a case referred to in the first sentence of Article 16(1) must be presented within a specific  time period that is at least three years from the first notification of the action resulting in taxation not in  accordance with the provisions of the Covered Tax Agreement. The combined effect of paragraphs 6(b)(i)  and 6(b)(ii) is that the second sentence of paragraph 1 will apply to a Covered Tax Agreement if either: (1)  all Contracting Jurisdictions to a Covered Tax Agreement make such a notification that the Covered Tax  Agreement provides for a time period shorter than three years; or (2) no Contracting Jurisdiction to a  Covered Tax Agreement makes such a notification that the Covered Tax Agreement provides for a time  period of at least three years. In all other cases, the second sentence of paragraph 1 shall apply to the  covered Tax Agreement, but shall supersede the existing provisions of the Covered Tax Agreement only to  the extent that those provisions are incompatible with the second sentence of paragraph 1.

205.  Paragraph 6(c)(i) requires each Party to notify the Depositary of the list of its Covered Tax  Agreements which do not contain provisions that provide that the competent authority that is presented  with the case by the person referred to in paragraph 1 shall endeavour, if the objection appears to it to be  justified and if it is not itself able to arrive at a satisfactory solution, to resolve the case by mutual  agreement with the competent authority of the other Contracting Jurisdiction, with a view to the avoidance  of taxation which is not in accordance with the Covered Tax Agreement. The first sentence of paragraph 2  shall apply to a Covered Tax Agreement only where all Contracting Jurisdictions to a Covered Tax  Agreement have made such a notification.

206.  Paragraph 6(c)(ii) provides that each Party (other than a Party that has reserved the right not to  apply the second sentence of paragraph 2) shall notify the Depositary of the list of its Covered Tax  Agreements which do not contain provisions that require any agreement reached to be implemented  notwithstanding any time limits in the domestic law of the Contracting Jurisdictions. The second sentence  of paragraph 2 shall apply to a Covered Tax Agreement only where all Contracting Jurisdictions to a  Covered Tax Agreement have made such a notification.

207.  Paragraph 6(d)(i) requires each Party to notify the Depositary of the list of its Covered Tax  Agreements which do not contain provisions that require the competent authorities of the Contracting  Jurisdictions to endeavour to resolve by mutual agreement any difficulties or doubts arising as to the  interpretation or application of the Covered Tax Agreement. The first sentence of paragraph 3 shall apply  to a Covered Tax Agreement only where all Contracting Jurisdictions to a Covered Tax Agreement have  made such a notification.

208.  Paragraph 6(d)(ii) requires each Party to notify the Depositary of the list of its Covered Tax  Agreements which do not contain provisions that provide that the competent authorities may also consult  together for the elimination of double taxation in cases not provided for in the Covered Tax Agreement.  The second sentence of paragraph 3 shall apply to a Covered Tax Agreement only where all Contracting  Jurisdictions to a Covered Tax Agreement have made such a notification.

Article 17 – Corresponding Adjustments

209.  Element 1.1 of the Action 14 minimum standard also provides that jurisdictions should provide  access to the mutual agreement procedure in transfer pricing cases and should implement the resulting  mutual agreements (e.g. by making appropriate adjustments to the tax assessed). The Action 14 Report  noted that it would be more efficient if jurisdictions also had the possibility to provide for corresponding  adjustments unilaterally in cases in which they find the objection of the taxpayer to be justified. In this  regard, Best Practice 1, contained in the Action 14 Report, states that jurisdictions should include Article  9(2) of the OECD Model Tax Convention in their tax treaties. Article 17 of the Convention provides a  mechanism for Parties to implement this Best Practice.

Paragraph 1

210.  Paragraph 1 is based on the text of Article 9(2) of the OECD Model Tax Convention. Changes  are made to the model text of Article 9(2) to conform the terminology used therein to the terminology used  in the Convention. Article 9(2) of the OECD Model Tax Convention reads as follows:

2.  Where a Contracting State includes in the profits of an enterprise of that State — and  taxes accordingly — profits on which an enterprise of the other Contracting State has been  charged to tax in that other State and the profits so included are profits which would have  accrued to the enterprise of the first-mentioned State if the conditions made between the two  enterprises had been those which would have been made between independent enterprises,  then that other State shall make an appropriate adjustment to the amount of the tax charged  therein on those profits. In determining such adjustment, due regard shall be had to the  other provisions of this Convention and the competent authorities of the Contracting States  shall if necessary consult each other.

Paragraph 2

211.  Paragraph 2 contains a compatibility clause which describes the relationship between Article  17(1) of the Convention and provisions of Covered Tax Agreements. It provides that Article 17(1) shall  apply to Covered Tax Agreements in the place or absence of a provision requiring that a Contracting  Jurisdiction shall make a corresponding adjustment where the other Contracting Jurisdiction makes an  adjustment that reflects the arm’s length profits of an enterprise. Such existing provisions would include,  for example, those modelled after Article 9(2) of the OECD Model Tax Convention or the UN Model Tax  Convention, and also include provisions which require agreement by the competent authority of a  Contracting Jurisdiction as a condition for making corresponding adjustment on the taxation by the other  Contracting Jurisdiction.

Paragraph 3

212.   The inclusion of Article 9(2) of the OECD Model Tax Convention in tax treaties is a best  practice under Action 14 and is not required as part of the Action 14 minimum standard. However, element  1.1 of the Action 14 minimum standard requires that jurisdictions provide access to the mutual agreement  procedure in transfer pricing cases and implement the resulting mutual agreements regardless of whether  the tax treaty contains a provision modelled after Article 9(2) of the OECD Model Tax Convention. To  reflect this, Article 17(3) allows a Party to reserve the right not to apply paragraph 1 only on the basis that  in the absence of the provisions described in Article 17(2) in Covered Tax Agreements, either (i) the Party  making the reservation will make the adjustment as referred to in Article 17(1); or (ii) its competent  authority will endeavour to resolve a transfer pricing case under the mutual agreement procedure provision  of its tax treaty. Where one Contracting Jurisdiction to a Covered Tax Agreement makes such a reservation  and the other Contracting Jurisdiction does not, Article 17 will not apply to the Covered Tax Agreement,  and there is no expectation created under the Convention that the Contracting Jurisdiction that has not  made the reservation will make a corresponding adjustment.

213.  A Party may also reserve the right for the Article not to apply to its Covered Tax Agreements that  already contain a provision of the same type (whether or not the provision adopts the precise language of  the OECD Model Tax Convention or the UN Model Tax Convention so long as the provision contains a  requirement that a Contracting Jurisdiction shall make a corresponding adjustment). Such a provision  would include, for example, a provision stating that a Contracting Jurisdiction shall make a corresponding  adjustment if it considers the adjustment justified, or that the corresponding adjustment shall be made if  there is an agreement reached between the competent authorities of the Contracting Jurisdictions. As  described above in paragraph 17, however, such a provision would not include one which merely provides,  for example, that the competent authorities of the Contracting Jurisdictions may consult together with a  view to reach an agreement on the adjustment of profits in both Contracting Jurisdictions or that provides  only that the Contracting Jurisdiction may make an appropriate adjustment. Paragraph 3 also provides for a  Party that has made a reservation under Article 16(5)(c)(ii) to reserve the right for Article 17 not to apply  to its Covered Tax Agreements on the basis that in its bilateral treaty negotiations it shall accept a treaty  provision of the type contained in paragraph 1, provided that the Contracting Jurisdictions were able to  reach agreement on that provision and on the provisions described in Article 16(5)(c)(ii).

Paragraph 4

214.  Paragraph 4 requires each Party (other than a Party that has made either of the reservations under  paragraph 3) to notify the Depositary of whether each of its Covered Tax Agreements contains an existing  requirement to make a corresponding adjustment, and if so, the article and paragraph number of each such  provision. The provisions of paragraph 1 will replace such provisions where all Contracting Jurisdictions to  a Covered Tax Agreement have made such a notification. In other cases, paragraph 1 will apply to the  Covered Tax Agreement, but will supersede existing provisions of a Covered Tax Agreement only to the  extent that those provisions are incompatible with paragraph 1.

Part VI. Arbitration

Article 18 – Choice to Apply Part VI

215.  Part VI of the Convention is intended to apply only between Parties that explicitly choose to  apply it. Article 18 allows a Party to choose to apply Part VI with respect to its Covered Tax Agreements  by notifying the Depositary of its choice. As between two Contracting Jurisdictions to a Covered Tax  Agreement, Part VI will apply only if both Contracting Jurisdictions notify the Depositary that they choose  to apply it.

Article 19 – Mandatory Binding Arbitration

Paragraph 1

216.  Paragraph 1 contains the core arbitration provision. It provides that, where the competent  authorities are unable to reach an agreement on a case pursuant to the mutual agreement procedure under  the Covered Tax Agreement within a period of two years, unresolved issues will, at the request of the  person who presented the case, be submitted to arbitration in the manner described in Part VI. This  arbitration process is available where, under the provisions of a Covered Tax Agreement relating to the  mutual agreement procedure (as they may be modified by Article 16(1)), a person has presented a case to  the competent authority of a Contracting Jurisdiction on the basis that the actions of one or both of the  Contracting Jurisdictions have resulted for that person in taxation not in accordance with the provisions of  the Covered Tax Agreement. The start date for this two-year period is determined pursuant to paragraph 8  or 9, as the case may be. The competent authorities may, however, agree to a different time period with  respect to a particular case, provided that they notify the person who presented the case of such agreement  prior to the expiration of the two-year period referred to in subparagraph b). This different time period with  respect to a particular case could be longer or shorter than the two-year period referred to in subparagraph  b), depending, for example, on the nature and complexity of the particular case. In addition, as noted below,  paragraph 11 permits a Party to reserve the right to substitute a three-year period for the two-year period  referred to in subparagraph b) for the purposes of applying Article 19 to its Covered Tax Agreements. A  Party is also permitted to formulate reservations with respect to the scope of cases that are eligible for  arbitration, as described below in the sections of this Explanatory Statement related to Article 28(2)  (subject to the acceptance of those reservations by the other Parties).

Paragraph 2

217.  As noted in paragraph 51 of the Action 14 Report, the mutual agreement procedure is available to  taxpayers irrespective of the judicial and administrative remedies provided by the domestic law of the  Contracting Jurisdictions. Most tax administrations, however, will require that one process take place  before the other, to ensure that a taxpayer’s case will not proceed through both the mutual agreement  procedure and a domestic court or administrative proceeding at the same time. To accommodate this  approach, paragraph 2 provides that the period provided in paragraph 1(b) will stop running where a  competent authority has suspended the mutual agreement process referred to in paragraph 1(a) because a  case with respect to one or more of the same issues is pending before a court or administrative tribunal.  The period will start running again when a final decision has been rendered by the court or administrative  tribunal or the case has been suspended or withdrawn. It should be noted, however, that where a Party  makes the reservation described in Article 19(12), the arbitration process will terminate if a decision is  rendered by the court or administrative tribunal during the period in which the arbitration process is  suspended.

218.  Paragraph 2 also provides that the period provided in paragraph 1(b) will stop running where a  person who presented a case and a competent authority have agreed to suspend the mutual agreement  process for any reason. This would apply, for example, where the taxpayer and the competent authority  have agreed to suspend the mutual agreement procedure due to serious illness or some other personal  hardship. The period would start running again once that suspension has been lifted.

Paragraph 3

219.  In some cases, after a taxpayer has provided the initial information needed to undertake  substantive consideration of the case, the competent authorities may need to request additional information  from the taxpayer. For example, after the period provided in paragraph 1(b) has begun and after further  analysis based on working the case, a competent authority may determine that it needs additional  information in respect of a particular structure or transaction in order to reach agreement on how to resolve  a remaining issue. In such cases, a failure by a person directly affected by the case (i.e., the person who  made the initial request for a mutual agreement procedure or a person whose tax liability is directly  affected by the case) to provide such additional information in a timely manner may delay or prevent the  competent authorities from being able to resolve the case. To address this, paragraph 3 provides that the  period provided in paragraph 1(b) shall be extended where both competent authorities agree that a person  directly affected by the case has failed to provide in a timely manner any additional material information  requested by either competent authority after the start of the period provided in paragraph 1(b). In that case  the period will be extended for an amount of time equal to the period beginning on the date by which the  information was requested, and ending on the date on which that information was ultimately provided.

Paragraph 4

220.  The arbitration process provided for by Part VI is intended to provide a mechanism for the  competent authorities to resolve issues that may otherwise prevent agreement with respect to cases under  the mutual agreement procedure. Given that the arbitration process is an extension of the mutual agreement  procedure that serves to enhance the effectiveness of the procedure, subparagraph a) provides that the  arbitration decision shall be implemented through the mutual agreement concerning a particular case. This  means that following the decision of the arbitration panel, the competent authorities will enter into a  mutual agreement that (except to the extent that Article 24 applies) reflects the outcome of the arbitration  decision. This subparagraph also provides that the arbitration decision is final, meaning that, subject to  subparagraph b)(ii), the arbitration decision cannot be changed, either by the competent authorities or by  the arbitration panel, unless the provisions of Article 24 apply to permit agreement on a different resolution.

221.  Subparagraph b) provides that the arbitration decision shall be binding on both Contracting  Jurisdictions except in three situations: (i) if a person directly affected by the case does not accept the  mutual agreement that implements the arbitration decision; (ii) if the arbitration decision is held to be  invalid by a final decision of the courts of one of the Contracting Jurisdictions; and (iii) if a person directly  affected by the case pursues litigation in any court or administrative tribunal on the issues which were  resolved in the mutual agreement implementing the arbitration decision. The term “final decision of the  courts” describes a decision that is not merely an interim order or decision. The decision can be at any  level of court in one of the Contracting Jurisdictions.

222.  Subparagraph b)(i) addresses the situation in which a person directly affected by the case does  not accept the mutual agreement that implements the arbitration decision. Where a mutual agreement is  reached before domestic remedies have been exhausted, the competent authorities may require, as a  condition for the finalisation or conclusion of the agreement, that the taxpayer renounce the exercise of  rights to domestic legal remedies with respect to the issues resolved through the mutual agreement on the  case. Without such a renunciation, a subsequent court decision could prevent the tax authorities from

implementing the agreement. As a result, a person directly affected by the case will be considered not to  accept the mutual agreement if that person does not withdraw from any domestic legal procedures or  otherwise terminate any pending court or administrative proceedings in a manner consistent with the  mutual agreement within 60 days after being notified of the mutual agreement implementing the arbitration  decision. Where the mutual agreement is not accepted, or is considered not to have been accepted, the case  shall not be eligible for any further consideration by the competent authorities.

223.  Subparagraph b)(ii) provides that if a final decision of the courts of one of the Contracting  Jurisdictions holds that the arbitration decision is invalid, the request for arbitration shall be considered not  to have been made and the arbitration process shall be considered not to have taken place (except for the  purposes of Article 21, related to confidentiality, and Article 25, related to the costs of arbitration  proceedings). This paragraph is not intended to provide independent grounds for the invalidation of an  arbitration decision where such grounds do not exist under the domestic laws of the Contracting  Jurisdictions. Instead, it is meant to ensure that where a court of one of the Contracting Jurisdictions  invalidates an arbitration decision based on such existing rules, the other Contracting Jurisdiction is not  bound to implement the decision. This may occur under the domestic laws of some jurisdictions, for  example, where there has been a procedural failure (e.g. a violation of the impartiality or independence  requirements applicable to arbitrators pursuant to Article 20, a breach of the applicable confidentiality  requirements pursuant to Article 21, or collusion between the taxpayer and one of the Contracting  Jurisdictions) that has materially affected the outcome of the arbitration process. It is not expected,  however, that a court would overturn an arbitration decision because it disagrees with the outcome of the  arbitration process. This subparagraph also provides that in such a case the taxpayer can make a new  request for arbitration unless the competent authorities agree that such a new request should not be  permitted. Such a new request may be made without waiting for the passing of the period provided in  paragraph 1(b), since such period will have already passed. It is expected that the competent authorities  would agree that such a request should not be permitted where the actions of the taxpayer were the main  reason for the invalidation of the arbitration decision.

224.  Subparagraph b)(iii) provides that the arbitration decision shall not be binding on either  Contracting Jurisdiction if the taxpayer pursues litigation in a court or administrative tribunal on issues that  were resolved in the mutual agreement implementing the arbitration decision. This subparagraph ensures  that where a Party is not permitted under its domestic law to require a taxpayer to agree to forego litigation  as part of accepting a decision under the mutual agreement procedure, that litigation cannot be used to  achieve non-taxation or reduced taxation, for example by asserting that the arbitration decision binds one  Contracting Jurisdiction while the outcome of the litigation binds the other.

Paragraphs 5 through 9

225.  Paragraphs 5 through 9 provide detailed rules to establish the start date of the period before a  case becomes eligible for arbitration. Paragraph 5 provides that the competent authority that received the  initial request for a mutual agreement procedure must, within two calendar months of receiving the initial  request for a mutual agreement procedure, notify the person who presented the case that the request has  been received, and send a notification of the request, along with a copy of the request, to the other  competent authority. Under paragraph 6, a competent authority must notify the person that presented the  case and the other competent authority that it has received all information necessary to undertake  substantive consideration of the case, or request additional information for that purpose from the person  that presented the case, within three calendar months from the date on which it received the initial request  or was notified of the request, as the case may be. As noted below in paragraph 229, the competent  authorities should settle between them the minimum information that each of them will require in order to  undertake substantive consideration of the case, and should publish a list of such information. The

competent authorities may also wish to settle other procedural matters related to the application of  paragraphs 5 through 9.

226.  Where one or both competent authorities request additional information, paragraph 7 provides  that after receiving such information, the competent authority requesting the information would have three  calendar months to notify the person presenting the case and the other competent authority that it has  received all necessary information, or that requested information is still missing.

227.  The start date of the period referred to in paragraph 1(b) depends on whether such additional  information has been requested. Where no request for additional information has been made, paragraph 8  provides that the start date is the earlier of: a) the date on which both competent authorities have notified  the person who presented the case that all necessary information was received (i.e., the date on which the  second of the two competent authorities has made that notification), and b) three calendar months after the  date on which the competent authority to which the request for a mutual agreement procedure was initially  made notified the other competent authority of the request.

228.  Where additional information was requested, paragraph 9 provides that, in general, the start date  is the earlier of: a) the latest date on which the competent authorities that requested additional information  have notified the taxpayer and the other competent authority that the information has been received; and b)  the date that is three calendar months after both competent authorities have received the additional  information from the person who presented the case. If either competent authority notifies the taxpayer and  the other competent authority that some of the requested information is still missing, such notification shall  be treated as a request for additional information.

Paragraph 10

229.  In recognition of the wide variety of legal and tax systems, and the fact that each competent  authority relationship is unique, paragraph 10 requires that the competent authorities of the Contracting  Jurisdictions settle the mode of application of the arbitration provisions by mutual agreement, including  (but not limited to) the minimum information necessary for each competent authority to undertake  substantive consideration of the case, before the date on which unresolved issues in a mutual agreement  procedure case are first eligible to be submitted to arbitration. Ordinarily, a Contracting Jurisdiction’s  published guidance would indicate the information that would be required for consideration of a request for  a mutual agreement procedure. In such cases, it is assumed that the competent authorities of the  Contracting Jurisdictions would generally mutually agree to list or otherwise identify the information  included in that guidance as the information that would be required by each Contracting Jurisdiction to  undertake substantive consideration of the case.

230.  While Part VI sets out the core provisions related to arbitration, as well as default rules to ensure  that the key structural elements of the process are in place, ensuring the smooth functioning of the  arbitration process will require close collaboration by the competent authorities to jointly agree on the  procedural and operational details of the arbitration process. It will be important for the competent  authorities to consult closely on these details in order to ensure that the mode of application of Part VI is  settled before unresolved issues in a mutual agreement procedure case are first eligible for arbitration. This  mode of application may be changed from time to time thereafter. In the absence of an agreement in  advance, competent authorities and taxpayers may experience difficulty and delay in progressing through  the arbitration process. It is expected that a model competent authority agreement that can be used as a  basis for this consultation will be produced. Examples of the types of details that should be agreed between  the competent authorities are described below in the explanatory text related to the other provisions of Part  VI.

Paragraph 11

231.  Paragraph 11 allows a Party to reserve the right to replace the two-year period set forth in  paragraph 1(b) with a three-year period for the purposes of applying Part VI to its Covered Tax  Agreements. Like other reservations to the Convention, where a Contracting Jurisdiction to a Covered Tax  Agreement makes this reservation, it will apply for the purposes of the application of that Covered Tax  Agreement by both Contracting Jurisdictions.

Paragraph 12

232.  In some jurisdictions a mutual agreement concluded by the competent authority cannot override  the decision of a court or administrative tribunal of that jurisdiction, either as a matter of law or as a matter  of administrative policy or practice. Those jurisdictions, or jurisdictions intending to adopt such a practice,  may wish to ensure that the arbitration process cannot be pursued with respect to issues that have been  resolved through domestic litigation, either before submission of the issues to arbitration or during the  arbitration process. Paragraph 12 addresses this issue by permitting a Party to reserve the right to exclude  from arbitration issues with respect to which a decision has been rendered by a court or administrative  tribunal of either Contracting Jurisdiction.

233.  In the case of a Covered Tax Agreement of a Contracting Jurisdiction which has made the  reservation described in paragraph 12, an unresolved issue shall not be submitted to arbitration if a decision  on that issue has already been rendered by a court or administrative tribunal of either Contracting  Jurisdiction. In addition, the arbitration process will terminate if a decision concerning the unresolved issue  is rendered by a court or administrative tribunal of one of the Contracting Jurisdictions at any time after a  request for arbitration has been made and before the arbitration decision has been delivered.

Article 20 – Appointment of Arbitrators

Paragraphs 1 and 2

234.  Paragraphs 1 and 2 set out basic rules for the composition of an arbitration panel and the  appointment and qualifications of arbitrators. While these rules would apply by default, paragraph 1 also  permits the competent authorities to mutually agree on different rules, either generally or with respect to a  particular case.

235.  Under paragraph 2, the arbitration panel is composed of three individual members. These  members must have expertise or experience in international tax matters, though, unless the competent  authorities agree otherwise, there is no requirement that each member have experience as a judge or an  arbitrator. One member is to be appointed by each competent authority within 60 days of the date of the  request for arbitration pursuant to Article 19(1). Those two members must then, within 60 days of the latter  of their appointments, appoint a third member who is not a national or resident of either Contracting  Jurisdiction to serve as Chair of the arbitration panel.

236.  Each member appointed to the arbitration panel must, at the time of accepting his or her  appointment, be impartial and independent of the competent authorities, tax administrations, and ministries  of finance (or relevant equivalent ministries or departments, regardless of their name) of the Contracting  Jurisdictions, as well as all persons directly affected by the case and their advisors. Each member must also  maintain his or her impartiality and independence throughout the proceedings, and must for a reasonable  period of time thereafter avoid conduct that may damage the appearance of impartiality and independence  of the members of the arbitration panel with respect to the proceedings. Such conduct would include, for  example, accepting employment with one of the persons directly affected by the case soon after delivering  the arbitration decision with respect to the case. In settling the mode of application of Part VI, the

competent authorities may wish to agree on additional details with respect to the applicable standards for  impartiality and independence. For example, the competent authorities may wish to require that any  prospective arbitration panel member disclose to the competent authorities any fact or circumstance likely  to call into question that prospective member’s impartiality or independence. The competent authorities  may also wish to agree to rules addressing the situation in which a panel member is unable to perform his  or her duties, as a result of illness or incapacity, failing to meet standards for impartiality and independence,  or any other reason.

Paragraphs 3 and 4

237.  Paragraphs 3 and 4 describe default rules which would apply in the case in which either  competent authority fails, within the prescribed time periods, to appoint an arbitrator, or in the case in  which two initial members of the arbitration panel fail to appoint a Chair. These paragraphs provide that, in  such cases, the appointment will be made by the highest ranking official of the Centre for Tax Policy and  Administration of the OECD that is not a national of either Contracting Jurisdiction. These default rules are  intended to ensure that arbitration, and therefore a resolution of the issues in a mutual agreement procedure  case, cannot be unduly delayed by a failure to constitute an arbitration panel. As default rules, the rules in  paragraphs 3 and 4 will apply only to the extent that the competent authorities have not mutually agreed on  different rules.

Article 21 – Confidentiality of Arbitration Proceedings

Paragraph 1

238.  To ensure that the arbitration process can accomplish its purpose without undermining the  confidentiality of the mutual agreement procedure, it is important that the competent authorities be  permitted to provide arbitrators with relevant information, subject to the same strict confidentiality  requirements that would apply to the competent authorities themselves. To accomplish this, paragraph 1  provides that, solely for the purposes of Part VI, the Covered Tax Agreement and the domestic laws of the  Contracting Jurisdictions related to the exchange of information, confidentiality, and administrative  assistance, the members of the arbitration panel shall be considered persons or authorities to whom  information may be disclosed. Pursuant to paragraph 1, such information may also be disclosed to  prospective arbitrators, but solely to the extent necessary to verify their ability to fulfil the requirements of  arbitrators, including, for example, their independence and impartiality. Paragraph 1 additionally provides  that information received by the arbitration panel or by prospective arbitrators, as well as any information  that the competent authorities may receive from the arbitration panel, shall be considered information  exchanged under the exchange of information and administrative assistance provisions of the Covered Tax  Agreement. Recognising the need to balance the goal of minimising the number of people to whom  information may be disclosed against arbitration panel members’ need for staff support, this paragraph also  provides for disclosure under the same conditions to a maximum of three staff per panel member.

Paragraph 2

239.  Paragraph 2 requires the competent authorities to ensure that members of the arbitration panel  and their staff agree in writing, prior to their acting in an arbitration proceeding, to treat any information  relating to the arbitration proceeding consistently with the confidentiality and nondisclosure requirements  under the provisions of the Covered Tax Agreement related to the exchange of information and  administrative assistance and under the applicable laws of the Contracting Jurisdictions. As part of the  agreement on the mode of application of Part VI under Article 19(10), the competent authorities may wish  to settle the details of this process, including which competent authority would obtain such written

agreement. The consequences of breaching such an agreement would be determined under the domestic  laws of the Contracting Jurisdictions and under the terms of the agreement.

Article 22 – Resolution of a Case Prior to the Conclusion of the Arbitration

240.  Recognising that the purpose of arbitration under Part VI is to resolve disputes between the  competent authorities arising from mutual agreement procedure cases, Article 22 provides that the mutual  agreement procedure, as well as the arbitration procedure, will terminate if, during the arbitration process  (at any time after a request for arbitration has been made and before the arbitration panel has delivered its  decision), either (i) the competent authorities come to a mutual agreement to resolve the case or (ii) the  taxpayer withdraws either its request for arbitration or its request for a mutual agreement procedure.

Article 23 – Type of Arbitration Process

Paragraph 1

241.  Paragraph 1 provides for default rules with respect to the type of arbitration process that will  apply for the purposes of arbitration proceedings pursuant to Part VI, but permits the competent authorities  of the Contracting Jurisdictions to mutually agree on different rules, which may apply to all cases or to a  particular case.

242.  By default, a “final offer” arbitration process (otherwise known as “last best offer” arbitration)  will apply, except to the extent that the competent authorities mutually agree on different rules. Under this  approach, the competent authorities will each submit to the arbitration panel a proposed resolution which  addresses all of the unresolved issues in the case in a manner that is consistent with any previous  agreements that have been reached in that case by the competent authorities. For each adjustment or similar  issue in the case, the proposed resolution will include only the disposition of specific monetary amounts  (for example, of income or expense) or the maximum rate of tax charged pursuant to the Covered Tax  Agreement. In some cases, however, unresolved issues will include questions regarding whether the  conditions for applying a provision of a Covered Tax Agreement have been met. Where the unresolved  issues in a case include such a “threshold question”, such as whether a person is a resident of a Contracting  Jurisdiction or whether an enterprise of one of the Contracting Jurisdictions has a permanent establishment  in the other Contracting Jurisdiction, the competent authorities may submit their proposed answers to the  threshold question (i.e. yes or no). If there are other unresolved issues the disposition of which is  contingent on the answer reached with respect to the threshold question, it is expected that the competent  authorities would also submit alternative proposed resolutions of those remaining issues.

243.  The proposed resolutions submitted by the competent authorities of each Contracting Jurisdiction  may be supported by a position paper. Each competent authority may also submit a reply submission with  respect to the proposed resolution and supporting position paper submitted by the other competent  authority. The reply submission and its supporting paper are meant to address only the positions and  arguments of the other competent authority, and are not intended as an opportunity for a competent  authority to advance additional arguments in favour of its own position. Paragraph 1(b) provides that each  competent authority that submits a proposed resolution, position paper or reply submission must provide a  copy to the other competent authority by the date on which such proposed resolution, position paper or  reply submission was due. Due dates for the proposed resolutions, position papers, and reply submissions,  along with other details with respect to these documents (such as, for example, their maximum length)  should be provided in the competent authority agreement on the mode of application of the arbitration  procedure entered into pursuant to Article 19(10). As part of that agreement, the competent authorities may  also wish to describe the process they will use to reach agreement on the issues to be resolved by the  arbitration panel.

244.  In the “final offer” arbitration process, the arbitration panel will select as its decision one of the  proposed resolutions submitted by the competent authorities. In a case involving one or more threshold  questions, the arbitration panel will decide the threshold question(s), and then adopt one of the alternative  proposed resolutions submitted by the competent authorities. The decision will be adopted by a simple  majority of the panel members, and will not include any rationale or explanation. In light of the purpose of  arbitration to act as a streamlined method for resolving disputes between the competent authorities, the  decision will be delivered in writing to the competent authorities and may not be used as precedent with  respect to any other cases.

Paragraph 2

245.  Under paragraph 2, a Party that is not willing to accept the “final offer” approach described in  paragraph 1 as a default rule may reserve the right not to apply paragraph 1 to its Covered Tax Agreements  and to adopt the “independent opinion” approach as the default type of arbitration process, except to the  extent that the competent authorities of the two Contracting Jurisdictions mutually agree on different rules,  which may apply to all cases or to a particular case. Under the “independent opinion” approach, each  competent authority must provide to the arbitration panel any information that the panel may consider  necessary to reach its decision. As part of the mutual agreement under Article 19(10), the competent  authorities may wish to describe the process they will use to reach agreement on the issues to be resolved  by the arbitration panel. The competent authorities may also agree, as part of the competent authority  agreement entered into pursuant to Article 19(10), that each competent authority may submit a supporting  position paper for consideration by the arbitration panel. Unless the competent authorities agree otherwise,  the arbitration panel may not take into account any information that was not available to both competent  authorities before both competent authorities received the request for arbitration.

246.  The arbitration panel will then decide the issues which have been submitted to arbitration in  accordance with the applicable provisions of the Covered Tax Agreement and, subject to those provisions,  those of the domestic laws of the Contracting Jurisdictions. In this regard, the arbitration panel would  review the application of domestic law only to the extent necessary to determine whether a Contracting  Jurisdiction correctly applied the Covered Tax Agreement. The competent authorities may also, by mutual  agreement, identify other sources of law or authority that will be considered by the arbitration panel.

247.  The decision of the arbitration panel will be presented to the competent authorities in writing,  indicating the sources of law relied upon and the reasoning which led to its result. It would also normally  include a description of the relevant facts and circumstances of the case, a clear statement of the positions  of both competent authorities, and a short summary of the proceedings. The adoption of the arbitration  decision will be by a simple majority of the panel members. As with the “final offer” approach, the  decision will have no precedential value.

Paragraph 3

248.   Where a Party that has chosen to apply Part VI has made the reservation permitted by paragraph  2 and another Party that has chosen to apply Part VI either (i) also makes the reservation permitted by  paragraph 2 or (ii) does nothing, the “independent opinion” approach will apply as between those two  Parties. Paragraph 3 accordingly provides a mechanism to address the situation in which two Parties have  differing, firmly-held views on their preferred type of arbitration process. Under paragraph 3, a Party that  has not reserved the right to apply the independent opinion approach as a default rule under paragraph  2may reserve the right for the default rules provided in paragraphs 1 and 2 not to apply with respect to its  Covered Tax Agreements with Parties that have reserved the right to apply the “independent opinion”  approach as a default rule in place of “final offer” arbitration. Where a Party has made the reservation  permitted by paragraph 3, it would be left to the competent authority of that Party and the competent

authority of the Party that made a reservation under paragraph 2 to determine the type of arbitration  process that would apply as between those two Parties.

249.  Where a reservation under paragraph 3 has been made by either Contracting Jurisdiction to a  Covered Tax Agreement, and where the other Contracting Jurisdiction has made a reservation under  paragraph 2, the competent authorities are required to endeavour to reach an agreement on the type of  arbitration process that will apply to all cases arising under the Covered Tax Agreement. Until such  agreement is reached, Article 19 will not apply. As a result, the competent authorities are not required to  consider a request for arbitration until such an agreement is reached.

Paragraphs 4 and 5

250.  Paragraph 4 provides that Parties may choose to apply paragraph 5 to their Covered Tax  Agreements. This paragraph is an optional provision which, subject to paragraphs 6 and 7, will apply  between two Contracting Jurisdictions to a Covered Tax Agreement if either Contracting Jurisdiction  chooses to apply it and notifies the Depositary accordingly. Paragraph 5 requires the competent authorities,  prior to the start of arbitration proceedings, to ensure that each taxpayer involved in the case and their  advisors agree in writing not to disclose any of the information received during the course of the arbitration  proceedings from either competent authority or from the arbitration panel. A material breach of this  agreement between the time at which the request for arbitration was made and before the arbitration panel  has delivered its decision will result in the termination of the mutual agreement procedure and the  arbitration proceedings with respect to the case.

Paragraphs 6 and 7

251.  Paragraph 6 allows a Party, other than a Party that has chosen to apply paragraph 5, to reserve the  right not to apply paragraph 5 with respect to one or more identified Covered Tax Agreements (or with  respect to all of its Covered Tax Agreements). A Party that has chosen to apply paragraph 5, however, may  reserve the right under paragraph 7 for Part VI not to apply at all with respect to any Covered Tax  Agreement for which the other Contracting Jurisdiction has made the reservation pursuant to paragraph 6.  The overall effect of paragraphs 4 through 7 is to ensure that where a Contracting Jurisdiction to a Covered  Tax Agreement has chosen to apply paragraph 5, taxpayers will be required to keep information received  during the arbitration process secret by default. Parties that do not consider this necessary, however, may  opt out of this requirement with respect to one or more Covered Tax Agreements. Parties that consider it  essential to require the taxpayer to maintain strict confidentiality, however, may opt out of arbitration  entirely with a Party that has opted out of the nondisclosure rule.

Article 24 – Agreement on a Different Resolution

Paragraphs 1 and 2

252.  Paragraph 1 permits a Party to choose to apply paragraph 2 with respect to its Covered Tax  Agreements. Notwithstanding Article 19(4), paragraph 2 allows the competent authorities to depart from  the arbitration decision and to agree on a different resolution within three calendar months after the  decision has been delivered to them. This may arise, for example, if the arbitration panel issues a decision  that both competent authorities consider to be an inappropriate resolution of the issues in the case.  Paragraph 2 is an optional provision and will be applied with respect to a Covered Tax Agreement only if  both Contracting Jurisdictions choose to apply it.

Paragraph 3

253.  Some jurisdictions consider that Article 24 would be unlikely to be applied where the “final offer”  approach described in Article 23(1) is used, given that under “final offer” arbitration, the arbitration  panel’s decision will be the position of one of the two competent authorities. To accommodate this view,  paragraph 3 therefore allows a Party that chooses to apply paragraph 2 to reserve the right for paragraph 2  to apply only with respect to its Covered Tax Agreements for which the “independent opinion” approach  described in Article 23(2) is applied.

Article 25 – Costs of Arbitration Proceedings

254.

255.  The competent authorities may also wish to reach agreement on a scale for the fees to be paid to  the members of the arbitration panel. They are free to agree to set such fees in a way that reflects the  particular circumstances of the Contracting Jurisdictions, their particular relationship, and the type of  arbitration process. In addition, in some jurisdictions, ratification procedures may require that estimated  costs connected to arbitration procedures be identified. For those jurisdictions, it may be necessary for the  competent authorities to agree on a schedule of fees in advance. Jurisdictions have used a variety of  schedules of fees as resources for this purpose, including the schedule of fees set by the International  Centre for Settlement of Investment Disputes and the schedule of fees provided in the Revised Code of  Conduct for the Convention of 23 July 1990 on the elimination of double taxation in connection with the  adjustment of profits of associated enterprises (the EU Arbitration Convention). Jurisdictions have also  limited the amount of travel and the number of days for which the panel members will be compensated.

Article 26 – Compatibility

Paragraph 1

256.  Paragraph 1 is a compatibility clause which describes the interaction between the provisions of  Part VI and provisions of Covered Tax Agreements that provide for arbitration of mutual agreement  procedure cases. This paragraph provides that the provisions of Part VI will apply to Covered Tax  Agreements that do not already provide for arbitration of unresolved issues arising from mutual agreement  procedure cases brought to the competent authorities by taxpayers. Part VI will also apply in place of  existing arbitration provisions that apply to issues arising from mutual agreement procedure cases (whether  they provide for mandatory binding arbitration or not), subject to the reservation in paragraph 4, described  below, which permits a Party to preserve the application of certain existing mandatory binding arbitration  provisions. Each Party that chooses to apply Part VI is required to notify the Depositary whether its  Covered Tax Agreements (other than those within the scope of a reservation under paragraph 4) contain

arbitration provisions (and, if so, the article and paragraph number of each such provision). It is expected  that in some cases, Contracting Jurisdictions to a Covered Tax Agreement that already provides for  mandatory binding arbitration will prefer to make the reservation described in paragraph 4 to preserve  those provisions. In other cases, as noted above in paragraphs 15 and 18, it is expected that the Contracting  Jurisdictions will use their best efforts to notify the Depositary of all existing provisions that provide for  the arbitration of unresolved issues arising from a mutual agreement procedure case. As a result, the  circumstance in which an existing arbitration provision is not identified is expected to be extremely rare.

Paragraph 2

257.  Paragraph 2 describes the interaction between the provisions of Part VI and the provisions of a  bilateral or multilateral convention that provides for the mandatory binding arbitration of unresolved issues  that arise from a mutual agreement procedure case. Given that a purpose of such conventions, like the  purpose of Part VI, is to resolve disputes efficiently and effectively, paragraph 2 avoids duplication of  efforts by providing that an unresolved issue arising from a mutual agreement procedure case will not be  submitted to arbitration under Part VI if an arbitration panel or similar body has previously been set up  with respect to the issue under another bilateral or multilateral convention that provides for the mandatory  binding arbitration of unresolved issues. Where an arbitration panel has not yet been set up under another  convention, however, Part VI would continue to apply to ensure that unresolved issues that arise in mutual  agreement procedure cases and that are eligible for submission to arbitration pursuant to Article 19 can be  resolved as quickly as possible.

Paragraph 3

258.  Paragraph 3 clarifies that the provisions of Part VI are not intended to affect the fulfilment of  wider obligations (e.g., obligations to resolve issues or cases that are not covered by Part VI) with respect  to the arbitration of unresolved issues arising in the context of a mutual agreement procedure resulting  from any conventions to which the Contracting Jurisdictions are or will become parties, other than  provisions of a Covered Tax Agreement which have been superseded by Part VI pursuant to paragraph 1.

Paragraph 4

259.  As noted above, paragraph 4 allows a Party to preserve existing mandatory binding arbitration  provisions by reserving the right for Part VI not to apply to one or more identified Covered Tax  Agreements (or to all of its Covered Tax Agreements) that provide for mandatory binding arbitration of  unresolved issues arising in a mutual agreement procedure case. In this context, a Covered Tax Agreement  would be considered to provide for “mandatory binding arbitration” if, under specific circumstances (such  as a request by a person who presented the case), the competent authorities are required to submit issues  arising in a mutual agreement procedure case that are not resolved after a specific amount of time to  arbitration, and the outcome of that arbitration is binding on the competent authorities.

Part VII. Final Provisions

Article 27 – Signature and Ratification, Acceptance or Approval

Paragraph 1

260.  Paragraph 1 provides that the Convention will be open for signature as of 31 December 2016. It  goes on to provide that the Convention is open for signature by all States.

261.  In addition, given that certain non-State jurisdictions have concluded tax agreements under the  arrangements with the State responsible for their international relations, the Convention is open for  signature by jurisdictions listed in subparagraph b). Following the name of each jurisdiction in  subparagraph b), the name of the State which is responsible for the international relations of that  jurisdiction is specified in parentheses. The inclusion of each jurisdiction listed in subparagraph b) was  authorised by the State responsible for its international relations and was agreed by the ad hoc Group.

262.  Finally, subparagraph c) provides that the Parties and Signatories may decide to authorise other  non-State jurisdictions to become Parties to the Convention following its opening for signature on 31  December 2016. This decision must be made by consensus, meaning that any jurisdiction which is not  listed in subparagraph b) can only become a Party to the Convention if no Party or Signatory objects.

Paragraph 2

263.  Paragraph 2 provides that signature of the Convention shall be followed by ratification,  acceptance or approval. The appropriate term will depend on domestic legal requirements. Once the  domestic procedures have been completed, an instrument of ratification, acceptance or approval must be  deposited with the Depositary and this is the event which triggers the rule for the entry into force of the  Convention pursuant to Article 34 of the Convention.

Article 28 – Reservations

Paragraph 1

264.  Paragraph 1 sets out a list of authorised reservations by reference to the provision in which they  are set out. With the exception of reservations to Part VI of the Convention which are governed by Article  28(2), these are the only reservations which may be made under the Convention.

Paragraph 2

265.   Paragraph 2(a) provides that any Party that chooses under Article 18 (Choice to Apply Part VI)  to apply Part VI (Arbitration) of the Convention may formulate one or more reservations with respect to  the scope of cases that shall be eligible for arbitration under Part VI. In developing Part VI, the Sub-Group  on Arbitration considered establishing a list of defined reservations with respect to the scope of cases. It  was considered, however, that while the certainty provided by such a list would be desirable, it was  unlikely that consensus could be reached on a list of defined reservations among all members of the Sub- Group. In addition, there was concern that if a Party had strong policy concerns with respect to particular  types of cases that were not listed (for example because that Party did not take part in the initial  development of Part VI), that Party might be unable to choose to apply Part VI despite a desire to commit  to mandatory binding arbitration for other types of cases. Paragraph 2 was therefore added to provide  Parties committing to arbitration with flexibility to tailor the scope of cases that will be eligible for  arbitration to reflect their domestic policies regarding arbitration.

266.   As provided in paragraph 5, a reservation under paragraph 2(a) would generally be made at the  time of signature or when depositing the instrument of ratification, acceptance or approval. For a Party that  does not choose to apply Part VI at the time it becomes a Party to the Convention, but chooses later to  apply Part VI by making a notification to the Depositary, however, reservations under paragraph 2(a) must  be made at the same time as the Party’s notification to the Depositary that it chooses to apply Part VI  pursuant to Article 18.

267.   Paragraph 2(b) provides that reservations made under paragraph 2(a) will be subject to  acceptance by the other Parties. It specifies that a reservation made under paragraph 2(a) shall be  considered to have been accepted by another Party if that other Party has not notified the Depositary that it  objects to the reservation by the end of a period of twelve calendar months beginning on the date of  notification of the reservation to all Parties and Signatories by the Depositary or by the date on which the  Party deposits its instrument of ratification, acceptance, or approval, whichever is later. For a Party that  does not choose to apply Part VI at the time it becomes a Party to the Convention, but chooses later to  apply Part VI by making a notification to the Depositary, however, objections to prior reservations made  by other Parties pursuant to subparagraph a) can be made at the time of the first-mentioned Party’s  notification to the Depositary that it chooses to apply Part VI pursuant to Article 18.

268.   In cases where a Party does raise an objection to a reservation made under paragraph 2(a), the  entirety of Part VI would not apply between the objecting Party and the reserving Party. Accordingly, it is  expected that Parties will carefully formulate their reservations under paragraph 2(a) as well as carefully  consider any objections to such reservations since the result of an objection to a reservation will be that  there is no basis for mandatory binding arbitration between those two Parties under the Convention.

269.   It should be noted as well that a Party is free to withdraw a reservation or replace it with a more  limited reservation pursuant to Article 28(9) at any time, and it is expected that Parties will continue to  evaluate their reservations over time to ensure that they continue to be consistent with the shared goal of  improving the resolution of disputes between the competent authorities.

Paragraph 3

270.  Paragraph 3 confirms the effect of reservations made under paragraph 1 or 2 on the application of  the relevant provisions of the Convention between the reserving Party and the other Parties to the  Convention. The paragraph states that unless explicitly provided otherwise, any reservation made by a  Party will modify the provisions to which it relates to the same extent for both the reserving Party and the  other Party. Accordingly, unless a provision of the Convention explicitly provides otherwise, a reservation  will modify the relevant provisions of the Convention as between the reserving Party and all other Parties  to the Convention, i.e. for the reserving Party in its relations with the other Parties and for those other  Parties in their relations with the reserving Party. In other words, reservations will apply symmetrically,  unless provided otherwise.

Paragraph 4

271.  Paragraph 4 requires a Party which has included, in its list of Covered Tax Agreements pursuant  to Article 2(1)(a) of the Convention, one or more tax agreements entered into by or on behalf of a  jurisdiction or territory for whose international relations it is responsible pursuant to Article 2(1)(a) of the  Convention, to deposit a separate list of reservations for that jurisdiction or territory, which may be  different from the Party’s own list of reservations. This separate list of reservations will apply to all  agreements entered into by or on behalf of that jurisdiction or territory which are covered by the  Convention.

272.  Paragraph 4 is not relevant to jurisdictions which become Parties to the Convention pursuant to

273.  The word “territory” is used in addition to “jurisdiction” in order to capture the various terms  used to refer to non-State entities for whose international relations a State is responsible. The words “by or  on behalf of” are also intended to capture the various ways in which a tax agreement may be concluded in  respect of a non-State jurisdiction or territory. In certain cases, the tax agreement may be entered into by  the jurisdiction or territory itself while, in other cases, the State which is responsible for the international  relations of the jurisdiction or territory may enter into the tax agreement on its behalf. In both situations,  the State Party responsible for the international relations of the jurisdiction or territory shall provide a list  of reservations in respect of that jurisdiction or territory, which may be different from the State Party’s  own list of reservations.

274.  If any reservations listed in Article 28(8) are made in respect of the jurisdiction or territory, the  Party shall also provide a list of the tax agreements entered into by or on behalf of that jurisdiction or  territory that are within the scope of the reservation. In all other cases, the list of reservations in respect of  the jurisdiction or territory shall apply to all tax agreements concluded by that jurisdiction or territory and  which are or later become Covered Tax Agreements, including agreements which are added in the future  pursuant to Article 29(5) of the Convention.

275.  The deposit by a Party of the list of reservations in respect of a jurisdiction or territory pursuant  to Article 28(4) shall take place either: i) at the same time as the deposit of the list of reservations of the  relevant Party if one or more tax agreements of the jurisdiction or territory are included in the Party’s  initial list of tax agreements pursuant to Article 2(1)(a)(ii); or ii) at the same time as the notification of an  extension of the list of agreements pursuant to Article 29(5) of the Convention if that extension includes  for the first time a tax agreement entered into by the jurisdiction or territory.

Paragraphs 5 through 7 – Timing of Reservations

276.  Paragraphs 5 through 7 set out the timing for making reservations under the Convention.  Essentially, the Convention requires that a provisional list of reservations be provided to the Depositary at  the time of signature and that a final list of reservations, subject to subsequent changes to that list which  are explicitly authorised by the provisions of Article 28(2), (5), and (9) and Article 29(5) of the Convention,  be provided to the Depositary at the time of the deposit of the instrument of ratification, acceptance or  approval. At the same time, the Convention allows for the possibility that a final list of reservations,  subject to subsequent changes to that list which are explicitly authorised by the provisions of Article 28(2),  (5), and (9) and Article 29(5) of the Convention, can be provided to the Depositary at the time of signature  (in such cases, the document containing the reservations must explicitly specify that it is to be considered  final).

Paragraph 5

277.  Paragraph 5 provides that reservations shall be made either at the time of signature or when  depositing an instrument of ratification, acceptance or approval. This general rule is subject to the  provisions of Article 28(2) (the possibility for a Party which chooses to apply Part VI to formulate one or  more reservations with respect to the scope of cases that shall be eligible for arbitration under the  provisions of Part VI), Article 28(6) (the possibility to provide a definitive list of reservations at the time of  signature), Article 28(9) (the possibility to withdraw or replace reservations) and Article 29(5) (the  possibility to make new reservations if an agreement added to the list notified under Article 2(1)(a)(ii) is  the first to fall within the scope of a reservation listed in Article 28(8) or if a newly added agreement is the

first inclusion in the list of a tax agreement entered into by or on behalf of a jurisdiction or territory for  whose international relations the Party is responsible). It is possible, however, for a Party to choose to  apply Part VI of the Convention after it has already become a Party. To ensure that such a Party has the  opportunity to make the defined reservations related to Part VI, paragraph 5 also provides that such  reservations shall be made at the time of that Party’s notification to the Depositary pursuant to Article 18  that it chooses to apply Part VI.

Paragraph 6

278.  Paragraph 6 provides that if reservations are made at the time of signature, they shall be  confirmed upon deposit of the instrument of ratification, acceptance or approval since this is the moment at  which consent to be bound by the Convention is expressed following the completion of domestic  procedures. At the time of the deposit of the instrument of ratification, acceptance or approval, changes  may be made to the list of reservations including the addition or deletion of reservations or the  modification of reservations made at the time of signature.

279.  Paragraph 6 provides for an exception in a case in which a Signatory explicitly specifies that the  list of reservations it makes at the time of signature is to be considered definitive. In such cases, no  confirmation of the reservations would be required upon deposit of the instrument of ratification,  acceptance or approval. The definitive nature of reservations made upon signature is, however, subject to  the provisions of Article 28(2) and (5) (the possibility for a Party which chooses to apply Part VI after it  has become a Party to the Convention to make the reservations permitted under Part VI at the time it  chooses to apply Part VI), Article 28(9) (the possibility to withdraw or replace reservations) and Article  29(5) (the possibility to make new reservations if an agreement added to the list notified under Article  2(1)(a)(ii) is the first to fall within the scope of a reservation listed in Article 28(8) or if a newly added  agreement is the first inclusion in the list of a tax agreement entered into by or on behalf of a jurisdiction or  territory for whose international relations the Party is responsible), dealt with below.

Paragraph 7

280.  Paragraph 7 provides that if reservations are not made at the time of signature, a provisional list  of expected reservations shall be provided to the Depositary at that time. This provisional list is for  transparency purposes only and is intended to give other Signatories a preliminary indication of the  Signatory’s intended position. This takes account of the nature of the Convention which will operate to  modify existing bilateral or multilateral relationships and the reservations chosen by the other Contracting  Jurisdictions will determine the way in which the existing bilateral or multilateral agreement is modified.  Accordingly, provisional indications of intended positions are important to allow an understanding of the  likely changes to an existing tax agreement and to facilitate domestic ratification procedures as well as to  prepare for the implementation of the modifications made by the Convention. The provisional list of  expected reservations under Article 28(7) does not restrict the ability of that Signatory to submit a  modified list of reservations upon deposit of the instrument of ratification, acceptance or approval.

Paragraph 8

281.  Paragraph 8 requires that, when reservations are made under the listed provisions, an exhaustive  list of the Covered Tax Agreements which are within the scope of the reservation as defined in the relevant  provision must be provided. In the case of a reservation that applies only where a Covered Tax Agreement  contains a specific type of provision, a list of the article and paragraph number of each relevant provision  must also be provided. This is intended to provide clarity as to the application of reservations which are  intended to apply only to Covered Tax Agreements with a specific characteristic. Such reservations would  not apply to any Covered Tax Agreement which is not included in the lists required by paragraph 8.

Paragraph 9

282.  Paragraph 9 provides for the possibility to withdraw a reservation made in accordance with

283.  Subparagraph a) applies where all Contracting Jurisdictions are States or jurisdictions which are  Parties to the Convention on the date of receipt by the Depositary of the notification of withdrawal or  replacement of the reservation. In line with the approach taken to the entry into effect of the Convention in

284.  Subparagraph a) sets out two categories: (i) reservations to provisions relating to taxes withheld  at source, and (ii) reservations to all other provisions.

285.  With respect to category (i), the first taxes in relation to which the withdrawal or replacement of a  reservation will have effect are those for which the event giving rise to the taxes occurs on or after 1  January of the next year following the expiration of a period of six calendar months beginning on the date  of the communication by the Depositary of the notification of the withdrawal or replacement to all Parties  and Signatories.

286.  For example, as illustrated in the timeline below, where a Party deposits a notification of  withdrawal of a reservation in respect of provisions relating to taxes withheld at source on 25 August 2018,  and the Depositary communicates this to all Parties and Signatories on 1 September 2018, the withdrawal  will be effective for any tax where the event giving rise to such tax occurs on or after 1 January 2020 (the  date of communication by the Depositary of 1 September 2018, plus expiration of the period of six  calendar months takes the timeline to 1 March 2019, thus the first taxes to which the withdrawal will apply  must relate to events occurring on or after 1 January the following year, i.e. 2020).

2018  2019  2020  25 August  1 September  6 month period  1 March 2019  1 January

Deposit  of  notification  of  withdrawal

Communication  to all Parties and  Signatories  by  Depositary

Expiration of 6  month period.

Withdrawal  of  reservation  will  have  effect with respect to all  withholding taxes which  relate  to  an  event  occurring from this date  onwards

287.  With respect to category (ii), the first taxes in relation to which the withdrawal of the reservation  will have effect are those which are levied with respect to periods beginning on or after 1 January of the  year next following the expiration of a period of six calendar months beginning on the date of the  communication by the Depositary of the notification of the withdrawal or replacement of the reservation.

288.  For example, as illustrated in the timeline below, where a Party deposits a notification of  withdrawal of a reservation in respect of all provisions other than those relating to taxes withheld at source  on 25 August 2018, and the Depositary communicates this to all Parties and Signatories on 1 September  2018, the withdrawal will be effective for any tax levied with respect to taxable periods beginning on or  after 1 January 2020 (the date of communication by the Depositary of 1 September 2018, plus expiration of  the period of six months takes the timeline to 1 March 2019, thus the first taxes to which the withdrawal  will apply will be those levied with respect to taxable periods beginning on or after 1 January the following  year, i.e. 2020).

2018  2019  2020  25 August  1 September  6 month

1 March 2019  1 January

period

Deposit  of  notification of  withdrawal

Withdrawal of reservation  will have effect with respect  to all non-withholding taxes  levied in respect of taxable  periods beginning on or after  1 January 2020

Communication  to all Parties  and Signatories  by Depositary

Expiration of 6  month period.

289.  Paragraph 9(b) applies with respect to Covered Tax Agreements for which one or more  Contracting Jurisdictions becomes a Party to the Convention after the date of receipt by the Depositary of  the notification of withdrawal or replacement of the reservation. In such cases, the withdrawal or  replacement shall take effect on the latest date on which the Convention enters into force for each of those  Contracting Jurisdictions. This takes into account the fact that, pursuant to Articles 34 and 35, there is at  least a three month period between the date of deposit of the instrument of ratification, acceptance or  approval and the entry into force of the Convention (i.e. the date on which a State or jurisdiction becomes a  Party) as well as an additional period before the provisions of the Convention enter into effect for the new  Party.

290.  With regard to Covered Tax Agreements entered into by or on behalf of a jurisdiction or territory  for whose international relations a Party is responsible and listed by that Party pursuant to Article  2(1)(a)(ii), the references in Article 28(9)(a) and (b) to a Party to the Convention and in Article 28(9)(b) to  the entry into force of the Convention for a Contracting Jurisdiction shall be read to refer to the Party  which is responsible for the international relations of that jurisdiction or territory.

291.

Article 29 - Notifications

Timing of Notifications

292.  Paragraphs 1, 3 and 4 set out the timing for making notifications under the Convention.  Essentially, the Convention requires that a provisional list of notifications be provided to the Depositary at

the time of signature and that a final list of notifications, subject to subsequent changes to that list which  are explicitly authorised by the provisions of Articles 29(5), 29(6) and 35(7) of the Convention, be  provided to the Depositary at the time of the deposit of the instrument of ratification, acceptance or  approval. At the same time, the Convention allows for the possibility that a final list of notifications,  subject to subsequent changes to that list which are explicitly authorised by the provisions of Articles 29(5),  29(6) and 35(7) of the Convention, can be provided to the Depositary at the time of signature (in such  cases, the document containing the notifications must explicitly specify that it is to be considered final).

Paragraph 1

293.  Paragraph 1 provides that notifications made pursuant to certain provisions in the Convention  shall be made either at the time of signature or when depositing the instrument of ratification, acceptance  or approval. This general rule applies subject to Article 29(5) (the possibility to extend the list of  agreements notified under Article 2(1)(a)(ii) and to make any additional notifications that may be required  in respect of the newly added agreements as well as to make new notifications if a newly added agreement  is the first inclusion in the list of a tax agreement entered into by or on behalf of a jurisdiction or territory  for whose international relations the Party is responsible); Article 29(6) (the possibility to make certain  additional notifications in respect of tax agreements already included in the list notified under Article  2(1)(a)(ii)); and Article 35(7) (the notifications required when a Party makes a reservation to the provisions  on entry into effect in order to allow for the completion of its internal procedures for that purpose).

294.  Paragraph 1 sets out an exhaustive list of the required notifications by reference to the provision  in which they are set out. These include notifications related to the choice of optional provisions, which  would apply with respect to all tax agreements entered into by a Party that are or may become Covered Tax  Agreements (subject to reservations applicable to Covered Tax Agreements that contain existing  provisions with specific, objectively defined characteristics). They also include notifications regarding  which of a Party’s Covered Tax Agreements are within the scope of the compatibility clauses for each  provision of the Convention.

Paragraph 2

295.  Paragraph 2 requires a Party which has included, in its list of Covered Tax Agreements pursuant  to Article 2(1)(a)(ii) of the Convention, one or more tax agreements entered into by or on behalf of a  jurisdiction or territory for whose international relations it is responsible pursuant to Article 2(1)(a)(i)(B)  of the Convention, to deposit a separate list of notifications for that jurisdiction or territory, which may be  different from the Party’s own list of notifications. This separate list of notifications will apply to all  agreements entered into by or on behalf of that jurisdiction or territory which are covered by the  Convention (subject to reservations applicable to Covered Tax Agreements that contain existing provisions  with specific, objectively defined characteristics).

296.  Paragraph 2 is not relevant to jurisdictions which become Parties to the Convention pursuant to

297.  The word “territory” is used in addition to “jurisdiction” in order to capture the various terms  used to refer to non-State entities for whose international relations a State is responsible. The words “by or  on behalf of” are also intended to capture the various ways in which a tax agreement may be concluded in  respect of a non-State jurisdiction or territory. In certain cases, the tax agreement may be entered into by  the jurisdiction or territory itself while, in other cases, the State which is responsible for the international  relations of the jurisdiction or territory may enter into the tax agreement on its behalf. In both situations,  the State Party responsible for the international relations of the jurisdiction or territory shall provide a list

of notifications in respect of that jurisdiction or territory, which may be different from the State Party’s  own list of notifications.

298.  Notifications related to the choice of optional provisions to be applied in respect of the  jurisdiction or territory shall apply to all tax agreements which are concluded by that jurisdiction or  territory and which are or later become Covered Tax Agreements, including agreements which are added  in the future pursuant to Article 29(5) of the Convention (subject to reservations applicable to Covered Tax  Agreements that contain existing provisions with specific, objectively defined characteristics).

299.  The deposit by a Party of the list of notifications in respect of a jurisdiction or territory pursuant  to Article 29(2) shall take place either: (i) at the same time as the deposit of the list of notifications of the  relevant Party if one or more tax agreements of the jurisdiction or territory are included in the Party’s  initial list of tax agreements pursuant to Article 2(1)(a)(ii); or (ii) at the same time as the notification of an  extension of the list of agreements pursuant to Article 29(5) of the Convention if that extension includes  for the first time a tax agreement entered into by the jurisdiction or territory.

Paragraph 3

300.  Paragraph 3 provides that if notifications are made at the time of signature, they shall be  confirmed upon deposit of the instrument of ratification, acceptance or approval since this is the moment at  which consent to be bound by the Convention is expressed following the completion of domestic  procedures. At the time of the deposit of the instrument of ratification, acceptance or approval, changes  may be made to the list of notifications including the addition or deletion of notifications or the  modification of notifications made at the time of signature.

301.  Paragraph 3 provides for an exception in a case in which a Party explicitly specifies that the list  of notifications it makes at the time of signature is to be considered definitive. In such cases, no  confirmation of the notifications would be required upon deposit of the instrument of ratification,  acceptance or approval. The definitive nature of notifications made upon signature is, however, subject to  the provisions of: Article 29(5) (the possibility to extend the list of agreements notified under Article  2(1)(a)(ii) and to make any additional notifications that may be required in respect of the newly added  agreements as well as to make new notifications if a newly added agreement is the first inclusion in the list  of a tax agreement entered into by or on behalf of a jurisdiction or territory for whose international  relations the Party is responsible); Article 29(6) (the possibility to make certain additional notifications in  respect of tax agreements already included in the list notified under Article 2(1)(a)(ii)); and Article 35(7)  (the notifications required when a Party makes a reservation to the provisions on entry into effect in order  to allow for the completion of its internal procedures for that purpose).

Paragraph 4

302.  Paragraph 4 provides that if notifications are not made at the time of signature, a provisional list  of expected notifications shall be provided to the Depositary at that time. This provisional list is for  transparency purposes only and is intended to give other Signatories a preliminary indication of the  Signatory’s intended position. This takes account of the nature of the Convention which will operate to  modify existing bilateral or multilateral relationships and the options chosen by the other Contracting  Jurisdictions will determine the way in which the existing bilateral or multilateral agreement is modified.  Accordingly, provisional indications of intended positions are important to allow an understanding of the  likely changes to an existing tax agreement and to facilitate domestic ratification procedures as well as to  prepare for the implementation of the modifications made by the Convention. The provisional list of  expected notifications under Article 29(4) does not restrict the ability of that Signatory to submit a  modified list of notifications upon deposit of the instrument of ratification, acceptance or approval.

Paragraph 5

303.  Paragraph 5 provides that the list of agreements notified under Article 2(1)(a)(ii) may be  extended at any time by means of a notification addressed to the Depositary. If the agreement falls within  the scope of any of the reservations made by the Party listed in Article 28(8), the Party must specify this in  this notification.

304.  The Party must also specify any additional notifications that are required under Article 29(1)(b)  through (s) to reflect the inclusion of the additional agreements. This would apply if the extension of the  list resulted in the inclusion of an agreement containing existing provisions falling within the scope of the  notifications required under Articles 3 through 26.

305.  In addition, as noted above, if the extension results for the first time in the inclusion of a tax  agreement entered into by or on behalf of a jurisdiction or territory for whose international relations a Party  is responsible, the Party shall specify at that time any reservations or notifications that would apply to  Covered Tax Agreements entered into by or on behalf of that jurisdiction or territory.

306.  Finally, paragraph 5 provides that, on the date on which a newly added agreement becomes a  Covered Tax Agreement under the Convention, the provisions on entry into effect in Article 35 will govern  the date on which the modifications to the Covered Tax Agreement will have effect.

Paragraph 6

307.  Paragraph 6 allows Parties to make additional notifications pursuant to Article 29(1)(b) through  (s) after becoming a Party to the Convention by means of a notification addressed to the Depositary.  Subparagraphs a) and b) set out when such additional notifications will take effect. The provision mirrors

308.  With regard to Covered Tax Agreements entered into by or on behalf of a jurisdiction or territory  for whose international relations a Party is responsible and listed by that Party pursuant to Article  2(1)(a)(ii), the references in Article 29(6)(a) and (b) to a Party to the Convention and in Article 29(6)(b) to  the entry into force of the Convention for a Contracting Jurisdiction shall be read to refer to the Party  which is responsible for the international relations of that jurisdiction or territory.

309.

Article 30 – Subsequent Modifications of Covered Tax Agreements

310.

Article 31 – Conference of the Parties

Paragraph 1

311.  Paragraph 1 provides that the Parties may convene a Conference of the Parties for the purposes of  taking any decisions or exercising any functions as may be required or appropriate under the provisions of

the Convention. This could include a Conference of the Parties to address questions of interpretation or  implementation of the Convention as foreseen in Article 32(2) or to consider a possible amendment to the  Convention as foreseen in Article 33(2).

312.  The Parties may decide to invite Signatories to participate in a Conference of the Parties. The  Conference of the Parties could meet in person, but could also fulfil its functions by meeting remotely, for  example by using videoconference or teleconference, by taking decisions through written procedure or by  any other means decided upon by the Parties.

Paragraph 2

313.  Paragraph 2 provides that a Conference of the Parties shall be served by the Depositary.

Paragraph 3

314.  Paragraph 3 provides that any Party may request a Conference of the Parties by communicating a  request to the Depositary. Thereafter, the Depositary will inform all Parties of such request. If the request  is supported by one-third of the Parties within six calendar months of the communication by the Depositary  of the request, the Depositary will convene a Conference of the Parties.

Article 32 – Interpretation and Implementation

Paragraph 1

315.  Paragraph 1 clarifies the mechanism for determining questions of the interpretation and  implementation of Covered Tax Agreements, as opposed to questions of the interpretation and  implementation of the Convention itself. Paragraph 1 provides that any questions as to the interpretation or  implementation of the provisions of a Covered Tax Agreement as modified by the Convention shall be  determined in accordance with the relevant provision(s) of that Covered Tax Agreement itself (as those  provisions may be modified by the Convention). Accordingly, the usual mechanisms foreseen by the  Covered Tax Agreement should be used to determine questions of interpretation and implementation of the  provisions of the Covered Tax Agreement which have been modified by the Convention. This would  include questions as to how the Convention has modified a specific Covered Tax Agreement pursuant to  the compatibility clauses and other provisions set out in the Convention. The competent authorities of the  Contracting Jurisdictions can therefore agree on the application of the Convention to their Covered Tax  Agreements, as long as the agreement reached is consistent with the provisions of the Convention.

Paragraph 2

316.  Paragraph 2 concerns the interpretation and implementation of the Convention itself and provides  that such questions may be addressed by a Conference of the Parties convened in accordance with the  procedure set out in Article 31(3). The word “may” is used in paragraph 2 since there could be other means  by which to address questions of interpretation and implementation of the Convention, such as the  competent authorities agreeing between themselves on how the Convention will operate in relation to a  particular Covered Tax Agreement.

317.  The final clause of the Convention provides the authentic languages of the Convention are  English and French. Accordingly, where questions of interpretation arise in relation to Covered Tax  Agreements concluded in other languages or in relation to translations of the Convention into other  languages, it may be necessary to refer back to the English or French authentic texts of the Convention.

Article 33 - Amendment

Paragraph 1

318.  Paragraph 1 provides that any Party can propose an amendment to the Convention by submitting  the proposed amendment to the Depositary.

Paragraph 2

319.  Paragraph 2 provides that a Conference of the Parties may be convened to consider the proposed  amendment in accordance with the procedure set out in Article 31(3).

Article 34 – Entry into Force

Paragraph 1

320.  Paragraph 1 provides that the Convention will enter into force on the first day of the month  following the expiration of a period of three calendar months beginning on the date of deposit of the fifth  instrument of ratification, acceptance or approval. As of that date, the five Signatories which have  deposited their instruments of ratification, acceptance or approval to the Convention will become Parties  and be bound by the Convention.

321.  In a case where the date of deposit of the fifth instrument of ratification, acceptance or approval  takes place on the first day of a month, “the first day of the month following the expiration of a period of  three calendar months beginning on the date of deposit” will be four months after the deposit of the  instrument or instruments of ratification, acceptance or approval. For example, if the fifth instrument of  ratification, acceptance or approval is deposited on 1 March 2018, the Convention will enter into force on 1  July 2018.

Paragraph 2

322.  Paragraph 2 provides that for each Signatory ratifying, accepting or approving the Convention  after the deposit of the fifth instrument of ratification, acceptance or approval, the Convention shall enter  into force for that State or jurisdiction on the first day of the month following the expiration of a period of  three calendar months after the date of the deposit by such State or jurisdiction of its instrument of  ratification, acceptance or approval. As of this date, such State or jurisdiction will be bound by the  Convention and its Covered Tax Agreements will be modified with effect from the date set out in Article  35.

323.  In a case where the date of deposit of the instrument of ratification, acceptance or approval takes  place on the first day of a month, the Convention will enter into force for that Signatory four months later  as described with respect to Article 34(1).

Article 35 – Entry into Effect

324.

Paragraph 1

325.

326.  Paragraph 1(a) relates to entry into effect of provisions of the Convention with respect to taxes  withheld at source on amounts paid or credited to non-residents. In this category, the first taxes for which  the provisions of the Convention will enter into effect are those for which the event giving rise to the tax  occurs on or after the first day of the next calendar year that begins on or after the latest of the dates on  which the Convention enters into force for each of the Contracting Jurisdictions to a Covered Tax  Agreement. For example, if the Convention enters into force for the first Contracting Jurisdiction on 1  March 2018 and for the second Contracting Jurisdiction on 1 March 2019, the Convention will take effect  with respect to all taxes which relate to an event occurring from 1 January 2020 onwards.

327.  Paragraph 1(b) relates to the entry into effect of provisions of the Convention with respect to all  other taxes levied by a Contracting Jurisdiction. In this category, the first taxes for which provisions of the  Convention will enter into effect are those which are levied with respect to taxable periods beginning on or  after the expiration of a period of six calendar months (or a shorter period, if all Contracting Jurisdictions  notify the Depositary that they intend to apply such shorter period) from the latest of the dates on which the  Convention enters into force for each of the Contracting Jurisdictions to a Covered Tax Agreement. For  example, where the Contracting Jurisdictions do not agree to apply a shorter period:

2018  2019  1 September  6  month  period

1 March 2019

Latest date of  entry into force  of  the  Convention for  each  of  the  Contracting  Jurisdictions to  a Covered Tax  Agreement

Expiration of 6 month period. The provisions of the Convention  will have effect with respect to all non-withholding taxes levied in  respect of taxable periods beginning on or after this date. In the  case of a taxable year that follows the calendar year, the  provisions of the Convention would have effect with respect to the  taxable period beginning 1 January 2020.

328.  With regard to Covered Tax Agreements entered into by or on behalf of a jurisdiction or territory  for whose international relations a Party is responsible and listed by that Party pursuant to Article  2(1)(a)(ii), the references in Article 35(1)(a) and (b) to the entry into force of the Convention for a  Contracting Jurisdiction shall be read to refer to the Party which is responsible for the international  relations of that jurisdiction or territory.

Paragraph 2

329.  Paragraph 2 provides that a Party may choose to substitute “taxable period” for “calendar year”  for the purposes of its own application of Article 35(1)(a) and (5)(a), and must notify the Depositary  accordingly if they do so. This will permit Contracting Jurisdictions to choose to link the entry into effect  of provisions related to withholding taxes to the taxable period, to address situations in which the taxable  period does not follow the calendar year.

330.  In such cases, for the entry into effect of the provisions of the Convention with respect to a  specific Covered Tax Agreement, the Party choosing this option shall apply the rule in paragraphs 1(a) and  5(a) with reference to its taxable period but the other Contracting Jurisdiction(s) can apply that rule with  reference to the calendar year (if they have not also chosen this option). Accordingly, the use of the word  “solely” at the beginning of paragraph 2 is intended to make clear that this choice would apply  asymmetrically and would apply only with respect to the application of paragraphs 1(a) and 5(a) by the  Contracting Jurisdiction that opted for it.

Paragraph 3

331.  Paragraph 3 provides that a Party may choose to replace the reference to “taxable periods  beginning on or after the expiration of a period” with a reference to “taxable periods beginning on or after  1 January of the next calendar year beginning on or after the expiration of a period” for the purposes of its  own application of Article 35(1)(b) and (5)(b), and must notify the Depositary accordingly if it does so.  This is to allow Contracting Jurisdictions to ensure that the entry into effect would take place only after the  start of a calendar year.

332.  In the same manner as paragraph 2, the word “solely” is intended to make clear that this option  may lead to asymmetrical entry into effect of the Convention’s provisions between Contracting  Jurisdictions.

Paragraph 4

333.  Paragraph 4 provides a specific rule for the entry into effect of Article 16 on Mutual Agreement  Procedure. Under this rule, Article 16 will have effect with respect to a Covered Tax Agreement for a case  presented to the competent authority of a Contracting Jurisdiction on or after the latest of the dates on  which the Convention enters into force for each of the Contracting Jurisdictions to the Covered Tax  Agreement, except for cases that were not eligible to be presented as of that date under the Covered Tax  Agreement prior to its modification by the Convention, without regard to the taxable period to which the  case relates. Paragraph 4 is intended to ensure that the provisions on Mutual Agreement Procedure apply as  soon as possible after the entry into force of the Convention, rather than applying only after expiry of the  period set out in paragraph 1, so that the provisions of Article 16 can apply to cases which are presented to  the competent authority after the entry into force of the Convention, even if they relate to taxable periods  prior to the entry into force of the Convention.

334.  The exception for cases which were not eligible to be presented for Mutual Agreement Procedure  prior to the entry into force of the Convention is intended to ensure that the Convention would not “revive”  cases which had been ineligible for Mutual Agreement Procedure prior to the entry into force of the  Convention.

Paragraph 5

335.  Paragraph 5 provides for the entry into effect in each Contracting Jurisdiction of the  Convention’s provisions for Covered Tax Agreements which result from an extension pursuant to Article  29(5) of the list of agreements notified under Article 2(1)(a)(ii). The time periods run similarly to those  described above with respect to paragraph 1, except that a time period of 30 days is added in subparagraph  a), and the time period in subparagraph b) is nine calendar months rather than six, and the time periods in  both cases start running as of the date of the communication by the Depositary of the notification of the  extension of the list of agreements, rather than from the latest of the dates of the entry into force of the  Convention for each of the Contracting Jurisdictions to the Covered Tax Agreement.

336.  As noted above, the choices set out in paragraphs 2 and 3 would also apply to the rule on entry  into effect set out in paragraph 5(a) and (b), respectively.

Paragraph 6

337.  Under paragraph 6, a Party may reserve the right for paragraph 4, which relates to the earlier  entry into effect of Article 16 on Mutual Agreement Procedure, not to apply with respect to its Covered  Tax Agreements. In such case, the entry into effect of Article 16 for a Covered Tax Agreement to which

Party which makes this reservation is a Contracting Jurisdiction will be governed by Article 35(1) through  (3).

Paragraph 7

338.  Paragraph 7 provides that a Party may reserve the right to delay the entry into effect of the  provisions of the Convention and thus the modification of Covered Tax Agreements until that Party has  completed its internal procedures for this purpose. In such cases, the rule on entry into effect set out in

339.  Mechanically, this is achieved by reserving the right to replace:

i)  specific sections of paragraphs 1, 4 and 5 such that the date from which the entry into effect of the  Convention is calculated is modified to be the date 30 days after the date of receipt by the  Depositary of the latest notification by each Contracting Jurisdiction making the reservation  described in paragraph 7 that it has completed its internal procedures for the entry into effect of the  provisions of the Convention with respect to that specific Covered Tax Agreement;

ii)  specific sections of Article 28(9) on Reservations which deal with the entry into effect of  withdrawals or replacements of reservations such that the date from which the entry into effect of  such withdrawal or replacement is calculated is modified to be the date 30 days after the date of  receipt by the Depositary of the latest notification by each Contracting Jurisdiction making the  reservation described in paragraph 7 that it has completed its internal procedures for the entry into  effect of the withdrawal or replacement of the reservation with respect to that specific Covered Tax  Agreement; and

iii)  specific sections of Article 29(6) on Notifications which deal with the entry into effect of  additional notifications under that paragraph such that the date from which the entry into effect of  such additional notifications is calculated is modified to be the date 30 days after the date of  receipt by the Depositary of the latest notification by each Contracting Jurisdiction making the  reservation described in paragraph 7 that it has completed its internal procedures for the entry into  effect of the additional notifications with respect to that specific Covered Tax Agreement.

iv)  specific sections of Article 36(1) through (5) which deal with the Entry into Effect of Part VI such  that the date from which the entry into effect of Part VI is calculated is modified to be:

a)  where a Party chooses to apply Part VI when it initially becomes a Party to the Convention,  the date 30 days after the date of receipt by the Depositary of the latest notification by each  Contracting Jurisdiction making the reservation described in paragraph 7 that it has  completed its internal procedures for the entry into effect of the provisions of the  Convention with respect to that specific Covered Tax Agreement; and

b)  where a Party begins applying Part VI to a Covered Tax Agreement only after it becomes a  Party to the Convention (because a new Covered Tax Agreement is added due to an  extension of the list of agreements of one or both Parties under Article 2(1)(a)(ii), because

of the withdrawal or replacement of a reservation made under Article 26(4) pursuant to

340.  Such a notification with respect to the entry into effect of the provisions of the Convention, the  withdrawal or replacement of a reservation, an additional notification, or the entry into effect of Part VI  would be required from a reserving Party with respect to each Covered Tax Agreement.

341.  An additional delay of 30 days between such notification and the entry into effect is provided for  practical reasons, to avoid the risk that the implementation of provisions could be required without  sufficient notice.

342.  The intention behind this reservation is to allow Parties which are required to amend their  domestic legislation to reflect the exact changes to their tax agreements to do so before the modifications  made by the Convention take effect. However, the clear understanding and expectation is that any Party  which makes this reservation will complete its internal procedures as expeditiously as possible in order to  fulfil its obligations under the Convention and minimise the delay in the entry into effect of the Convention  in relation to its Covered Tax Agreements.

343.  Subparagraph b) provides that the Party which made the reservation shall notify the confirmation  of the completion of its internal procedures simultaneously to the Depositary and the other Contracting  Jurisdiction(s) to the Covered Tax Agreement to which the notification relates. This is important in order to  provide the other Contracting Jurisdiction(s) with notice as early as possible as to when the timelines for  entry into effect will start running with respect to the Covered Tax Agreement. If a Contracting Jurisdiction  that has made the reservation under Article 35(7) does not have internal procedures to complete with  respect to a particular change of reservations or notifications, it is expected that that Contracting  Jurisdiction would immediately inform the Depositary and the other Contracting Jurisdiction that its  domestic procedures are completed for the purposes of this paragraph.

344.  Subparagraph c) provides that Article 35(7) shall apply symmetrically as between all Contracting  Jurisdictions to a Covered Tax Agreement. It states that where one or more Contracting Jurisdictions to a  Covered Tax Agreement makes a reservation under paragraph 7, the date of entry into effect of the  provisions of the Convention, of the withdrawal or replacement of a reservation pursuant to Article 28(9),  of an additional notification pursuant to Article 29(6) with respect to that Covered Tax Agreement, or of  the entry into effect of Part VI pursuant to Article 36, shall be governed by Article 35(7) for all Contracting  Jurisdictions to the Covered Tax Agreement. As such, if any Contracting Jurisdiction to a Covered Tax  Agreement makes the reservation set out in paragraph 7, the modified timelines for entry into effect will  apply to all Contracting Jurisdictions to the Covered Tax Agreement.

Article 36 – Entry into Effect of Part VI

Paragraph 1

345.   Paragraph 1 provides that notwithstanding the provisions of Article 28(9) (addressing the  withdrawal of a reservation), Article 29(6) (addressing additional notifications), and Article 35 (other than  paragraph 7) (addressing the entry into effect of the Convention), Article 36 shall govern the entry into  effect of the provisions of Part VI of the Convention.

346.  Subparagraph a) provides that Part VI will have effect with respect to cases presented to the  competent authority of a Contracting Jurisdiction on or after the later of the dates on which the Convention  enters into force for each of the Contracting Jurisdictions.

347.   Subparagraph b) provides that Part VI will have effect with respect to cases presented to the  competent authority of a Contracting Jurisdiction prior to the later of the dates on which the Convention  enters into force for each of the Contracting Jurisdictions, on the date on which both Contracting  Jurisdictions have notified the Depositary that they have reached mutual agreement on the application of  Part VI pursuant to Article 19(10), along with information regarding the date or dates on which such cases  shall be considered to have been presented to the competent authority of a Contracting Jurisdiction  according to the terms of that mutual agreement. For this purpose, the date on which both Contracting  Jurisdictions have notified the Depositary that they have reached mutual agreement on the application of  Part VI pursuant to Article 19(10) is the date on which the Depositary has received the notification from  the second Contracting Jurisdiction. With respect to the date on which such cases shall be considered to  have been presented, the competent authorities of the Contracting Jurisdictions can agree on a date which  applies to all cases or a specific date for each individual case. Communication to the Depositary of dates  with respect to individual cases, however, may require an anonymisation process in order to avoid  breaching confidentiality of taxpayer information. Alternatively, a Contracting Jurisdiction may  communicate the specific dates to the taxpayers directly, and simply notify the Depositary of the fact that  an agreement on dates with respect to individual cases has been reached, without providing details on those  individual cases. Subparagraph b) is intended to allow competent authorities to delay the eligibility of  existing cases until they have agreed the mode of application of Part VI, and to spread out the dates on  which such cases become eligible for arbitration, so all existing cases do not become eligible for arbitration  on the same day.

Paragraph 2

348.   Paragraph 2 provides that Parties may reserve the right for Part VI to apply to a case presented to  the competent authority of a Contracting Jurisdiction prior to the later of the dates on which the  Convention enters into force for each of the Contracting Jurisdictions only to the extent that the competent  authorities of both Contracting Jurisdictions agree that it will apply to that specific case. Where a Party has  made this reservation, its existing stock of mutual agreement procedure cases would not be covered unless  the competent authorities both agree that a particular existing case may be submitted to arbitration. Among  other things, this is intended to address concerns that resource constraints may make it challenging for  Contracting Jurisdictions with a large backlog of cases to apply Part VI effectively to those cases, despite  the ability under paragraph 1(b) to defer eligibility for arbitration.

349.  With regard to Covered Tax Agreements entered into by or on behalf of a jurisdiction or territory  for whose international relations a Party is responsible and listed by that Party pursuant to Article  2(1)(a)(ii), the references in Article 36(1)(a) and (b) and Article 36(2) to the entry into force of the  Convention for a Contracting Jurisdiction shall be read to refer to the Party which is responsible for the  international relations of that jurisdiction or territory.

Paragraphs 3 through 5

350.   Paragraphs 3 through 5 address the entry into effect of Part VI in the case in which a Party  begins applying Part VI to a Covered Tax Agreement only after it becomes a Party to the Convention. This  can arise because a new Covered Tax Agreement is added due to an extension by either Contracting  Jurisdiction of the list of agreements notified under Article 2(1)(a)(ii). It can also arise because of the  withdrawal of a reservation under Article 26(4) not to apply Part VI with respect to a specific Covered Tax  Agreement, or the replacement of such a reservation with one that is more limited in scope (e.g. by

replacing a reservation with respect to all Covered Tax Agreements with one that applies only to particular  Covered Tax Agreement). In addition, it can arise where a Party that previously objected to a reservation  formulated under Article 28(2) withdraws that objection. Finally, it can arise because a Party changes its  policy regarding arbitration and chooses to apply Part VI to its Covered Tax Agreements for the first time  after it becomes a Party. In all such cases, the date of entry into effect is based on the date of  communication by the Depositary of the relevant notification, withdrawal or replacement of reservation, or  withdrawal of objection, rather than the date of entry into force of the Convention.

Article 37 - Withdrawal

Paragraph 1

351.  Paragraph 1 provides that any Party may withdraw from the Convention at any time by means of  a notification addressed to the Depositary.

Paragraph 2

352.  Paragraph 2 provides that withdrawal will be effective as of the date on which the Depositary  receives the notification.

353.  Paragraph 2 also provides that in cases where the Convention has entered into force with respect  to all Contracting Jurisdictions to a Covered Tax Agreement before the date on which a Party’s withdrawal  becomes effective, that Covered Tax Agreement shall remain as modified by the Convention. Accordingly,  the effects of withdrawal are forward-looking only. That is, where the Convention has already modified a  Covered Tax Agreement (and regardless of whether those modifications have come into effect pursuant to

354.  Withdrawal would ensure that the Convention would not modify any tax agreements with States  and jurisdictions that join the Convention after the date of withdrawal since they would not fall within the  definition of “Covered Tax Agreements”.

355.  With regard to Covered Tax Agreements entered into by or on behalf of a jurisdiction or territory  for whose international relations a Party is responsible and listed by that Party pursuant to Article  2(1)(a)(ii), the reference in Article 37(2) to the entry into force of the Convention for a Contracting  Jurisdiction shall be read to refer to the Party which is responsible for the international relations of that  jurisdiction or territory.

Article 38 – Relation with Protocols

356.

Article 39 – Depositary

Paragraph 1

357.  Paragraph 1 provides that the Secretary-General of the Organisation for Economic Co-operation  and Development is the Depositary of the Convention and any protocols pursuant to Article 38.

Paragraph 2

358.  Paragraph 2 sets out a non-exhaustive list of the acts, notifications or communications in relation  to the Convention of which the Depositary will notify all Parties and Signatories. The Depositary must  notify the Parties and Signatories within one calendar month of the act, notification or communication.

Paragraph 3

359.  Paragraph 3 provides that the Depositary shall maintain publicly available lists of Covered Tax  Agreements, reservations made by Parties, and notifications made by Parties.

ANNEX

## ACTION REPORTS CONTAINING TAX TREATY-RELATED BEPS MEASURES ADDRESSED BY PROVISIONS OF THE CONVENTION

The following are the Action Reports that contain the substance of the tax treaty-related BEPS  measures agreed as part of the Final BEPS Package. Each measure is addressed in Articles 3 through 26 of  the Convention.

1.  Neutralising the Effects of Hybrid Mismatch Arrangements, Action 2 - 2015 Final Report  (Published on 5 October 2015)

Tax Treaty-Related BEPS Measure  Related Article  of the Convention

Dual-resident entities (page 137)

Treaty provision on transparent entities (page 139)

Exemption method (page 146), and Credit method (page 147)

2.  Preventing the Granting of Treaty Benefits in Inappropriate Circumstances, Action 6 - 2015  Final Report (Published on 5 October 2015)

Tax Treaty-Related BEPS Measure  Related Article  of the Convention

Limitation-on-benefits rule (page 20)

Rules aimed at arrangements one of the principal purposes of which is to  obtain treaty benefits (page 54)

Article 7  (paragraphs 1 and 4)

Dividend transfer transactions (page 70)

Transactions that circumvent the application of Article 13(4) (page 71)

Tie-breaker rule for determining the treaty residence of dual-resident  persons other than individuals (page 72)

Anti-abuse rule for permanent establishments situated in third States  (page 75)

Application of tax treaties to restrict a Contracting State’s right to tax its  own residents (page 86)

Clarification that tax treaties are not intended to be used to generate  double non-taxation (page 91)  Preamble and Article 6

3.  Preventing the Artificial Avoidance of Permanent Establishment Status, Action 7 - 2015 Final  Report (Published on 5 October 2015)

Tax Treaty-Related BEPS Measure  Related Article  of the Convention

Artificial avoidance of PE status through commissionnaire arrangements  and similar strategies (page 15)  Articles 12 and 15

Artificial avoidance of PE status through the specific activity exemptions  (page 28)

Splitting-up of contracts (page 42)

4.  Making Dispute Resolution Mechanisms More Effective, Action 14 - 2015 Final Report  (Published on 5 October 2015)

Tax Treaty-Related BEPS Measure  Related Article  of the Convention

Elements of a minimum standard to ensure the timely, effective and  efficient resolution of treaty-related disputes (page 13), and best practices  (page 28)

Articles 16 and 17

Commitment to mandatory binding MAP arbitration (page 41)  Articles 18 through 26
