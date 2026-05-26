---
tags: ["3.0"]
itaa-lex-sectie: ""
wet: "IBA Negotiated M&A Guide — Belgium 2022 (English) — Gisèle Rosselle + Céderic Devroey (Strelia, Brussels)"
bron_rol: "praktijkgids"
status: "beschikbaar"
bijgewerkt: "2022"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/IBA-MA-Belgium-2022.pdf
      sha256: 845a3ec1a67d228c1fb0a824b8ad3a36ed1f4b32506efe64f05bf9c0ae8ce9be
      version: '2022'
      pages:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 0c77206e-dirty
    model:
    prompt_version:
  generated_at: '2026-05-19T17:34:41Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-19T17:36:55Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Inhoudelijk coherente, volledige praktijkgids over Belgisch M&A-recht (BCCA, deal structuren, R&W, merger control, sluitingsformaliteiten). Structuur is zwak (5 #####-headings, sub-secties als plain text), maar de paragraph-cut chunker compenseert dit afdoende; alle headings bevatten substantiële tekst. Pagina-nummers als inline tekst (bv. '4 /35') en dubbele spaties na regeleinden zijn standaard pymupdf-artefacten die retrieval niet schaden."
    caveat:
    layer1:
      status: warn
      run_id: 20260519-173441
      run_at: '2026-05-19T17:34:41Z'
      heading_count: 5
      max_section_chars: 59798
      file_size_chars: 105649
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op #####-niveau: 59798 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-19T17:36:55Z'
      rationale: "Inhoudelijk coherente, volledige praktijkgids over Belgisch M&A-recht (BCCA, deal structuren, R&W, merger control, sluitingsformaliteiten). Structuur is zwak (5 #####-headings, sub-secties als plain text), maar de paragraph-cut chunker compenseert dit afdoende; alle headings bevatten substantiële tekst. Pagina-nummers als inline tekst (bv. '4 /35') en dubbele spaties na regeleinden zijn standaard pymupdf-artefacten die retrieval niet schaden."
      concrete_problemen:
        - Pagina-markers ('2 /35', '3 /35', etc.) zijn inline in de tekst terechtgekomen — lichte ruis per alinea maar niet blokkerend
        - Voetnootnummers en -tekst staan inline (bv. voetnoot 2 op regel 116) zonder afscheiding — beïnvloedt leesbaarheid van die passage
        - 'Zwakke heading-hiërarchie: sub-secties 1.1, 1.2.x, 2.x, 3.x, 4.x zijn plain text i.p.v. Markdown headings — chunker herstelt dit via paragraph-cut op de lange sectie (59798 chars)'
---

# IBA Negotiated M&A Guide — Belgium 2022 (English) — Gisèle Rosselle + Céderic Devroey (Strelia, Brussels)

*Bijgewerkt tot en met 2022 — gecoördineerde versie.*

##### 1.  INTRODUCTION

1.1  Belgian M&A market insights

The Covid-19 pandemic had a major impact on many Belgian M&A transactions in 2020,  especially from mid-March 2020 when the Belgian Federal Government mandated the first  nationwide lockdown. This caused many deal processes to suffer unanticipated delays or  suspensions, some even permanently.

Although certain sectors (such as tourism, aviation, energy, etc.) were hit hard by the pandemic,  the overall Belgian M&A market recovered quickly. Analysts remain bullish about it, and it is  safe to say that enterprises in certain sectors (such as healthcare, tech, the stay-at-home market,  etc.) have even been able to use the market effects of the pandemic to their advantage. In the  second half of 2020, during the summer following the relaxation of the containment measures,  interest in those markets grew. The number of deals multiplied impressively, and deal values  gained a significant uptick.

Just as in many M&A markets around the world, the pandemic has left its mark on the Belgian  M&A market. It has done this in different ways, such as affecting transaction documentation.  Surveys show that the Covid-19 pandemic impact has found its way into agreements, with as  many as one in five acquisition agreements containing Covid-related clauses (such as shifting  deadlines for conditions precedent, adding qualifications to the representations and warranties,  adding impact-of-Covid-19 exceptions to material adverse change (MAC) definitions, and adding  specific exceptions to leakage). There are other notable developments too, including: the increase  in auctions, locked-box pricing mechanisms, deferred payments, MAC clauses, and an increased  usage of warranty and indemnity (W&I) insurance.

Covid-19 certainly gave rise to many market predictions, but not all of them came true. Contrary to  what was predicted for the second half of 2020 and the beginning of 2021, there was no increase in  assets deals on the Belgian M&A market. Many practitioners expected a significant rise in the  number of bankruptcies and distressed M&A, but with the Belgian legislature’s introduction of a  bankruptcy moratorium, and with government financial support and other relief measures on an  unprecedented scale, far fewer businesses became insolvent than previously foreseen.

In the first half of 2021, Belgian enterprises continued to attract private equity firms and strategic  dealmakers. Driven by growth objectives and a search for high multiples, investors continue to  look for targets on the Belgian market to execute their buy-and-build strategies.

1.2  Recent developments in law

There have been many new developments in Belgian law since 2019. Many have or will have a  significant effect on M&A deals. Below are the most important changes that are relevant to M&A.

1.2.1 A new code for companies and associations

The Belgian Federal Parliament adopted the new Belgian Company and Associations Code  (BCCA) in March 2019. This new law aims to modernise Belgian corporate law and compete  with other jurisdictions. The BCCA will gradually replace the Belgian Companies Code  completely, given that its predecessor dates from 1999. We highlight some key changes that are  relevant to the M&A market.

2 /35

The main types of Belgian companies

The legislature was intended to simplify Belgian corporate law: it reduced the number of types of  companies that can be incorporated in Belgium to engage in business activities. The BCCA  permits four main company types, while the others (from the Company Code of 1999) have either  been abolished or allowed to continue to exist as a subtype of one of the four main types. The  legislature also made the four main company types more flexible.    BV/SRL ( besloten vennootschap/société à responsabilité limitée )

This limited liability company type (BV/SRL) has replaced the former BVBA/SPRL ( besloten  vennootschap met beperkte aansprakelijkheid/société privée à responsabilité limitée ). It has been  put forward as the reference company type.

The BV/SRL does not have required share capital, but rather equity ( eigen vermogen/fonds  propres ) only. No share capital means stricter rules apply to all kinds of distributions. For example,  distribution is authorised only if both of the following are met:

(i)  if the net assets are not and will not become negative as a result of the distribution; and  (ii)  if, according to reasonably foreseeable developments, the company will still be able to  meet its obligations over a twelve-month period after the distribution.

Founders and shareholders are free to structure the rights that are attached to shares. For instance,  they can issue shares with multiple voting rights and shares with rights to a preferential dividend.  Shares that have different rights attached to them than other shares constitute separate classes (see  the Securities section below). The legislature therefore abolished the old company law’s  prohibition of the BVBA/SPRL entity type from issuing classes of shares.

If a BV/SRL’s bylaws provide for this possibility, then a shareholder’s exit (ie, withdrawal or  exclusion) can take place at the expense of the company’s assets.

Given the flexibility of the BV, as highlighted above due to the BCCA, there have been more  incorporations of BV/SRLs than in the past. It is expected that founders will resort to incorporating  the NV/SA type of entity only for very large companies or for listed companies.

NV/SA (naamloze vennootschap/société anonyme)

As part of the company law reform, the legislature made the public limited liability company type  (NV/SA) more flexible, albeit with some restrictions due to mandatory EU laws that apply to the  NV/SA. One example of this flexibility is the fact that an NV/SA can now have a sole director. This  company type requires a minimum capital of €61,500, which must be fully paid up at the time of  incorporation, and 25 per cent of every share that has been issued in return for a contribution of  cash must also be fully paid up.

Although shares of a BV/SRL can also be listed on a stock exchange, the NV/SA continues to be  the archetypal company type for very large companies and listed corporations. Both a BV/SRL  and an NV/SA can be incorporated by one person. The two other company types (not addressed in  this guide) are the CV/SC ( cooperatieve vennootschap/société cooperative ) and the partnership  ( maatschap/société de droit commun ), which require three and two founders, respectively. 1

3 /35

This guide will focus on the BV/SRL and the NV/SA company types because they are the most  relevant to M&A.

Freedom to structure rights attached to shares and securities

For non-listed companies, the BCCA no longer requires that there be proportionality between the  voting rights attached to a share and the shareholder's share in the capital (one share, one vote). It  gives shareholders a lot of discretion to structure the rights that are attached to shares, eg, the  company could issue shares with multiple voting rights, preferential dividends, etc. In other words,  besides the mandatory rule that a company must issue at least one share with one vote, the only  limit is your imagination. 2

Parties to an M&A transaction must be mindful that, when you create shares with different rights  attached to them compared to other shares that have already been issued, those newly created  shares become a separate class ( soort/classe ) of shares based on the rights attached to them.  Issuance of a new share class requires compliance with a specific procedure set out in the BCCA.  This entails the adoption of a special board report and a report drawn up by the statutory auditor  ( commissaris/commissaire ) or business auditor ( bedrijfsrevisor/réviseur d'entreprise ) if financial  data underpins the board report. Any changes to the rights attached to share classes, or a share  issuance that does not occur proportionately in each class, requires the two abovementioned  reports to be drawn up, and decisions on them must be approved by a majority of 75 per cent in  each class. This means that a minority shareholder holding 25 per cent plus one vote has the power  to veto decisions.

Furthermore, both company types, the public limited liability company (NV/SA) and the private  limited liability company (BV/SRL), can issue all types of securities that are not prohibited by  law.

Restrictions on share transfers

The Company Code of 1999 prohibited founders and shareholders from changing the rules on  transferability of shares in a BV/SRL by making them less strict than what was imposed by law.  The BCCA radically changes this, allowing the transfer of shares in a BV/SRL to be made freely  or with restrictions. As a default rule in an NV/SA, shares can be transferred freely, yet founders  and shareholders can impose restrictions on the transferability of shares on condition that the  restrictions satisfy a legitimate interest, especially in terms of their validity period. The Company  Code of 1999 required that share transfer restrictions be in the interest of the company, and made  it possible for that interest in question to be assessed at any time. Now the legitimate interest is  assessed at the time when the restriction on share transfers is agreed upon.

Share transfer restrictions can be stipulated in a company’s articles of association, a deed of  issuance and other agreements. Further, the BCCA requires that share registers stipulate the

types without legal personality that were permitted under the Company Code of 1999. They were a partnership, a temporary  company, and a secret company. The BCCA has now merged them into one generic entity type – partnership. A partnership  requires two founders. It is often used as part of real estate planning and in construction. This company form is transparent  from a tax perspective.  2 Different rules apply to listed companies, where shares with multiple voting rights are prohibited and the issuance of shares  will need to comply with the principle of proportionality of voting rights, ie, the voting rights attached to each share should be  proportionate to their respective par value (fractiewaarde/pair comptable) .

4 /35

transfer restrictions that are set out in the articles of association.

A transfer that violates a transfer restriction in the articles of association is not enforceable against  the company and other third parties, regardless of the good faith of the transferee. However, a  transfer that violates a transfer restriction under a shareholders' agreement is enforceable against  the company or other third parties, which means that the company will have to recognise the  transferee as a shareholder. If the transferee was aware of the transfer restriction, then the other  shareholders can seek annulment of the transfer (sale) by applying to the court.

Leonine clause

Joint venture agreements and shareholders’ agreements often include put options that allow a  shareholder to sell its shares to the other shareholders at a price equal to at least the initial  investment. The validity of such options under the Company Code of 1999 was debated as it was  argued that these put options contravened the ban on leonine clauses ( leeuwenbeding/clause  leonine ), which is set out in Article 32 of the Company Code of 1999. This provision prohibits  clauses that exempt monies or goods contributed to the company by one or more shareholders  from any contribution to the loss and/or the profits of the company. Under the BCCA, a  shareholder cannot be exempt from any profit-sharing that is related to the shares, but the  shareholder can be exempt from bearing their share in the losses.

Financial assistance

Financial assistance is still restricted by law, but breaches of the rules on it are no longer a criminal  offence.

The BCCA requires that financial assistance meet the following conditions:

(a)  the assistance is authorised by a prior resolution of the general meeting;  (b)  the amount of the assistance can be distributed based on the net assets test (and liquidity  test 4 );  (c)  the board of directors draws up a special report on the assistance; and  (d)  the amount of the assistance is recorded as an unavailable reserve in the balance sheet.

The financial assistance procedure remains very strict. In practice, parties typically try to structure  around it in order to avoid the strict procedure under law.

Governance

The BCCA abolishes the mandatory character of the revocation ad nutum principle, whereby the  general meeting may revoke a director's mandate at any time without having to pay the director  an indemnity or give a notice period. Under the BCCA, a company's articles of association, or its  appointment decision, can stipulate that a director may be dismissed only if the company serves a  specified notice period or pays the director an indemnity. 5

5 /35

Regarding corporate governance, the law gives parties wide discretion to determine how a  company should be governed, depending on its needs. An NV/SA is considered the most  sophisticated company type because it has three governance models to choose from:

(a)  a collegial board of directors ( raad van bestuur/conseil d’administration );  (b)  a dual system that consists of a supervisory board ( raad van toezicht/conseil de  surveillance ) and a management board ( directieraad/conseil de direction ); or  (c)  the sole director model ( enige bestuurder/administrateur unique ).

The BV/SRL founders can opt for a governance model with one or more directors who act as a  collegial body or not. The dual system is therefore not available to a BV/SRL.

Online meeting attendance

The pandemic prevented companies from holding their general shareholders’ meetings in person.  This caused companies to quickly turn to remote conferencing, with or without video. Although  many companies’ articles of associations stipulated that an in-person gathering should be  organised, they did not foresee the possibility of allowing shareholders to attend the general  meeting online. Having regard to the effects of the pandemic, the legislature, in its Act of 20  December 2020, gave company boards of directors the possibility to allow shareholders to attend  the meetings online without the need for articles of associations to require any specific  authorisation.

The electronic means of communication used or the means for the shareholder to attend the  meeting online must enable the company to verify the capacity and identity of the person partaking  in the meeting. Moreover, the tool must also at least enable participants to take direct,  simultaneous, and uninterrupted note of the meeting – and, in principle, allow them to exercise  their right to vote and ask questions. However, a meeting is not allowed to be held completely  online. Belgian company law requires the members of the bureau (which is made up of the chair and,  if applicable, one or more secretaries and persons counting the votes) to be present in person at the  place where the general meeting is held. This because they are the ones who are in charge of the  redaction and signing of the minutes of the general meeting, as well as being responsible on behalf  of the company for the valid composition and organisation of the meeting in which remote  shareholders can participate.

Liability of directors

The BCCA caps directors’ liability towards the company and third parties at a certain value, which  ranges between €125,000 and €12m based on the company's turnover. The cap covers one or more  facts, or a series of related facts, that could give rise to liability of the directors, regardless of the  number of claimants or claims brought against the directors. The cap applies to all directors  together but it does not apply if the claim relates to minor errors that are committed habitually,  gross errors and late payment of certain taxes. Given these exceptions to the application of the  cap, a corporate group typically takes out directors and officers (D&O) liability insurance.

Actual-seat doctrine abolished

The BCCA abolished the actual-seat doctrine and laid down the statutory-seat doctrine instead: if  a company's statutory seat is in Belgium, then the applicable lex societas is the BCCA. In  principle, the BCCA does not apply to legal entities whose statutory seat is outside Belgium.

6 /35

Electronic shareholders’ register

Modernising and digitalising Belgian company law was one of the priority intentions of the  legislature. The Royal Decree implementing the BCCA therefore introduced the possibility for a  BV/SRL, NV/SA, and CV/SC to create an electronic register for shares and other securities that  the company has issued. However, to safeguard legal certainty, the legislature imposed strict  requirements for creating and keeping electronic registers.

Digital incorporation of companies

Since 1 August 2021, companies can be incorporated digitally. This means founders do not have  to appear in person before a notary to incorporate a Belgian company. The incorporation deed can  be signed electronically during a video conference with the notary.

1.2.2 UBO Register

The Belgian Act of 18 September 2017 created a centralised register ( Register van ultieme  begunstigden/Registre des bénéficiaires effectifs ) of ultimate beneficial owners (UBOs). It obliges  a company's management body to register its UBOs in the specifically designated register. 6 UBOs  are natural persons who (1) hold, directly or indirectly, a sufficient percentage of the voting rights  or ownership interest in the company or (2) who control the company through other means. Any  natural person who holds an interest of more than 25 per cent of the voting rights or more than 25  per cent of the shares is considered an indication of a sufficient percentage of the voting rights. If  no such natural persons can be identified, then the executives of the parent entity that holds a  sufficient percentage in the company have to be recorded as UBOs. 7 The UBO register is managed  by the Federal Public Service Finance.

1.2.3 Reform of the Civil Code

A new Civil Code (New Civil Code), containing nine books, 8 was enacted in April 2019. Since  then, its predecessor, the Civil Code of 21 March 1804, has been renamed the ‘Old Civil Code’  ( Oud Burgerlijk Wetboek/Ancien Code Civil ). For the time being, only two of these books have  come into force, namely Book 8 on Evidence and Book 3 on Goods. The New Civil Code clarifies  certain concepts and anchors new ones that have been laid down by case-law or doctrine. For  example, Book 5 on Contracts & Obligations creates a statutory framework for the transfer of  contracts, which is relevant in asset deals.

1.2.4 B2B legislation prohibiting unfair clauses

Just as consumers are protected against an imbalance in bargaining power, the Belgian legislature  sought to limit the bargaining power of companies by prohibiting clauses that create a ‘significant  imbalance’ between contracting enterprises.

In April 2019, the Belgian Federal Parliament adopted a new law prohibiting unfair clauses in  agreements between enterprises (B2B Law). This law introduced new provisions in the Code on  Economic Law ( Wetboek Economisch Recht/Code de droit économique ) and applies to all B2B

9. Statute of Limitations.

7 /35

agreements signed, amended, or renewed after 1 December 2020.

The scope of application of the B2B Law is broad.

The legislature did not define the concept of significant imbalance deliberately, so it could be a  catch-all provision. The fact that an acquisition agreement has been heavily negotiated would not  prevent a judge from finding one or more of the contractual clauses or the agreement as a whole  to be imbalanced. To mitigate such risk, parties in practice tend to stipulate in the preamble that  all parties to the contract acknowledge and accept that the contract is well-balanced.

Because the B2B Law applies to all agreements between enterprises and bans clauses and  contracts that create a significant imbalance between parties, it would apply to earn-out  mechanisms, option agreements, representations and warranties, and specific indemnities, which  are all key subject-matters in any M&A transaction.    Parties could seek to minimise the risk of a clause being declared unfair (and hence null and void),  by documenting their negotiations on the concessions made by each party and/or by stipulating in  the agreement the concessions that have been made reciprocally.

1.2.5 E-signatures

The Belgian Federal Parliament has enacted various laws to transpose the European Union’s  Electronic Identification, Authentication and Trust Services (eIDAS) Regulation's new  provisions into a comprehensive Belgian legal framework. These laws include the Act of 21 July  2016 amending the Code of Economic Law and the New Civil Code (in particular, Book 8 on  Evidence).

Belgian law now recognises the possibility for agreements and other documents to be validly  signed electronically. It distinguishes between qualified e-signatures, advanced and ordinary  signatures.

1.2.6 Foreign Direct Investment Screening Committee

The foreign direct investment (FDI) screening mechanisms that allow a country to monitor,  investigate, assess, condition, prohibit, or unwind an investment made by a foreign investor are  set out below.

Current FDI framework in Belgium

Although Belgium does not have a nationwide FDI screening mechanism, it does have a limited  one in place in the Flemish region. Article III.59 to III.60 of the Flemish Governance Decree of 7  December 2018 ( Bestuursdecreet ) allows the Flemish Government to annul any legal act whose  effects are that:

8 /35

(i)  the foreign natural person or foreign legal person concerned obtain control or obtain  decision-making power over a Flemish governmental body, entity, or agency  (including those at municipal and provincial levels and other government-controlled  entity); 10 and whereby  (ii)  the strategic interests of the Flemish community or the Flemish region become  threatened.

The Flemish Governance Decree's use of the term legal act implies that the decree applies to all  types of transactions, including share deals, asset deals and any other transaction type through  which a foreign entity (ie, any non-Belgian entity, EU or non-EU investors) obtains control.

The Flemish FDI screening mechanism is not limited to specific sectors, but it is clearly narrow  in scope as point (i) refers only to public institutions and authorities that are controlled by the  Flemish government.

Future FDI frameworks in Belgium

Following the adoption of an EU Regulation on FDI in 2019, the Belgian Federal Government is  in the process of drafting a bill of law to introduce an ex ante FDI screening mechanism at a federal  level. It will have a broad scope and is expected to apply to investments made by foreign investors  from non-EU countries that intend to invest in several strategic sectors such as energy, healthcare,  transportation, communications, defence and key infrastructure. The new law, if adopted, is  expected to create a new commission at the Federal Public Service of Economic Affairs that will  oversee screening potentially ‘harmful’ investments in certain key sectors. Because this bill of  law is still being refined behind closed doors in the Cabinet of the Minister of Economic Affairs,  any information available regarding this topic at Belgian level is very limited.

1.2.7 Environmental, social and corporate governance (ESG)

The ever-growing importance of ESG cannot be ignored. This is simply because investors are  increasingly applying these non-financial factors as part of their analysis and decision-making,  especially during the due diligence phase of an M&A transaction.

Article 3:6 of the BCCA requires a company to add in its annual report an analysis that ‘includes  key performance indicators that are both financial and, if appropriate, non-financial in nature and,  if appropriate, non-financial key performance indicators relating to the specific business of the  company, plus information on issues pertaining to the environment and staff.’ This information  should fall under the section on the company’s development and the risks and uncertainties that  the company is facing, to the extent necessary for the understanding of the business development.

1.3  Legal framework for private M&A transactions

The BCCA governs Belgian corporate law matters, such as the transfer of shares, the powers of  corporate bodies, as well as the various procedures on corporate restructurings.

Besides these new provisions, which are relevant to M&A, the general law of obligations on a  sale–purchase transaction laid down in the Civil Code are also relevant. National and EU  competition laws come into play if a merger filing is required to consummate the transaction. See  section 6.2.1 for more on merger control and antitrust clearance.

9 /35

Furthermore, the obligations to inform and consult employees about an M&A transaction (see  section 6.2.4) can also come into play. Tax legislation and other specific laws and regulations  regarding the transfer of real property (including soil remediation), transfer of permits, transfer of  intellectual property, and privacy and data protection will also have to be taken into account by the  parties.

Data shows that, across deal value, the acquisition agreement regarding Belgian targets or assets  is usually governed by Belgian law. An asset deal or share deal can be governed by foreign law,  but the local formalities under Belgian law must be complied with. These include the recording of  the transfer of the shares in the share register and registering the real estate in the mortgage register.  Further, if it is an asset deal and if the parties want to benefit from the automatic transfer of  liabilities, then they will have to follow the BCCA corporate restructuring procedures on, eg, the  transfer of a branch of activity, the contribution or the transfer of a universality, and mergers.    Relevant federal authorities and regulators

There is no general obligation to seek approval from a Belgian government authority to complete  a transaction, unless the transaction should go through the FDI screening mechanism (in  Flanders), which is very limited in scope (see section 1.2.6), and unless the transaction meets the  relevant thresholds and must therefore be notified to the Belgian competition authority. For certain  specific sectors, regulators can be required. For example, the National Bank of Belgium must  approve a merger in advance if it concerns payment institutions or the transfer of a payment  institution.

1.4  Buyers’ or sellers’ market?

Given the prevailing seller’s market, there has been an increase in the use of competitive auctions  across all deal values. Therefore, it is no surprise that sellers have been pushing back hard on the  execution risk, and the burden has often been put on the buyer by introducing ‘hell or high water’  clauses and reverse break fees. This sellers’ market has a clear impact on certain key terms such  as the increasing use of locked-box accounts to the detriment of closing accounts, minimum and  cap levels, escrow levels, conditions precedent (as defined below in section 2.1), representations  and warranties and specific indemnities, and the use of warranty and indemnity insurance.

2.  TYPES  OF  TRANSACTION  STRUCTURES  USED  IN  PRIVATE  M&A  TRANSACTIONS

2.1  General

Private M&A transactions can be performed in one or two steps. One-step transactions can be  signed and closed on the same day. In two-step transactions, the closing depends on conditions  precedent ( opschortende voorwaarden/conditions suspensives ) (CPs), such as obtaining certain  approvals, permits/authorisations, and licences.

In Belgium, a private M&A transaction is generally structured as (1) a share deal (ie, a purchase  of the target’s shares in exchange for cash consideration or shares) or (2) an asset deal (ie, a  purchase of the target's assets in exchange for cash consideration or shares, or both). Asset deals  can be performed as a means of a sale and purchase under the Civil Code, or can be transferred  under a BCCA procedure.

However, many transactions cannot be classified as a mere share deal or an asset deal because  they are of a hybrid nature. This is especially true in the current M&A landscape in which parties  want to focus on their core business. Imposing the performance of a carve-out as a CP has become  quite common (see common CPs under section 6.1). The following is a more detailed explanation  about share deals and asset deals.

2.1.1 Share deal

In a share deal, the buyer acquires the shares of the target (and possibly control over it as well),  but the target will remain the owner of its assets and liabilities.

There are two types of share deals: (1) an acquisition of the target's existing shares and (2) an  ‘acquisition’ of the target's new shares that have been issued through a capital or equity increase.  The second type is not a sale and purchase sensu stricto , but a capital or equity increase, which is  a type of transaction that is governed by the BCCA.

2.1.2 Asset deal

General

In some situations, it might be more advantageous for a buyer to not acquire the target's shares  but to acquire its assets and liabilities instead (see section 2.2.1).

Belgian law allows assets to be transferred one by one ( transfer ut singuli ) as a sale and purchase  or under one of the corporate transfer procedures provided for by the BCCA. These are:

(a)  a transfer of a branch of activity ( de overdracht van bedrijfstak/le transfert d'une branche  d'activité ) or  (b)  a transfer of a universality of goods ( de overdracht van algemeenheid/le transfert d’une  universalité ).    The BCCA defines a branch of activity as ‘a business unit that conducts activity autonomously  from a technical and operational perspective and that is capable of functioning by itself’, and a  universality of goods is ‘the entirety of the assets and liabilities of the company’. The question  whether assets characterise a branch of activity or whether they are a mere collection of assets  depends mainly on whether the entity is technically and administratively independent from the  company and can function on its own.

Authorised decision-making bodies

In principle, the seller's board of directors is authorised to decide on the transfer of the assets and  liabilities without the need to involve the general meeting of shareholders. However, the general  meeting will have to approve the transfer if: (1) the company's articles of association stipulate  this, or if (3) the transferor (seller) and the transferee (buyer) choose to follow the BCCA's  corporate procedure for a transfer of a universality of goods or a contribution of a branch of

activity.

Procedure

The formalities that are required for a transfer of assets depend on how the to-be-transferred assets  and liabilities are categorised and whether a BCCA corporate procedure is used.

The transfer ut singuli of each asset is a transfer whereby the buyer ‘cherry-picks’ the asset for  the transfer. What is ‘picked’ could even constitute a branch of activities or a universality of  goods. Such transfer must be made in accordance with the provisions of the Civil Code concerning  a sale and purchase.

The transfer ut universali of the assets that are considered a branch of activity or a universality of  goods does not have to be done through a detailed corporate procedure prescribed by the BCCA,  as this is not mandatory. The parties can decide to transfer a branch of activity under the provisions  of the Civil Code.

A transfer under the BCCA corporate procedure consists of two main phases and takes at least six  weeks. In the first phase, the board of directors of both the buyer and seller must draft an authentic  or private instrument proposing the transfer/contribution. This must then be filed with the clerk’s  office of the Court of Enterprises that has jurisdiction (ie, the court with jurisdiction over the  judicial district where the target is located) at least six weeks before the transfer/contribution and,  if appropriate, before the transferor’s (seller’s) general shareholders’ meeting, which will decide  on the transfer/contribution. The transferor’s board of directors must draft a written report on the  state of the assets explaining and justifying the following:    (a) the desirability of the transfer or contribution from legal and economic points of view;  (b) the conditions and manner of the transfer or the contribution; and  (c) the consequences of the transfer/contribution.    An excerpt from this report must be sent to the registered shareholders at least one month before  the general meeting. In the second phase, the transferor's general shareholders’ meeting will  decide on the transfer/contribution. If the buyer (transferee) treats the transfer/contribution of  assets as a capital increase, it will have to comply with the applicable provisions of the BCCA.  These provisions impose additional reporting obligations and require a decision from the buyer’s  general shareholders’ meeting about the transfer/contribution.

As indicated above, if the to-be-transferred assets of the target are categorised as a branch of  activity or a universality of goods, the parties can choose to have the assets transferred either (1)  under the BCCA corporate procedure or (2) as a sale and purchase under the Civil Code.

If the actual asset transfer amounts to a transfer of a complete or part of an undertaking  ( overdracht van een onderneming/transfert d'une entreprise ) as referred to in Collective  Bargaining Agreement no. 32bis (CBA 32bis), then the employment contracts of the relevant  employees (ie, all rights and obligations under those contracts) are transferred automatically to  the transferee (except for certain rights, such as supplementary provident schemes (pension, death  and incapacity insurance). For more information on the duty to inform and consult employees in  this type of transfer, see section 6.2.4.

2.2  Overview of the two transaction structures

Whether the transaction is a share deal or asset deal, they each have their pros and cons. There  are also factors that enable the parties to choose which transaction type is most appropriate.

2.2.1 Pros and cons

Share deal

One of the advantages of a share deal is that it is generally easy to execute because there will  usually be no disentanglement issues with any of the target's assets that are not transferred.    The disadvantages are mainly two-fold: (1) the buyer acquires all assets and liabilities subject to  the carving-out of certain activities before closing, and (2) a buyer of shares has limited legal  protection under the Civil Code (see section 2.2.2 below). To reduce the effect of these  disadvantages in a share deal, one should therefore draft the representations and warranties very  carefully and include a non-competition clause in the share purchase agreement.

Asset deal    If a BCCA transfer procedure is used, all the target's assets and liabilities are (in theory)  transferred automatically. This means the branch of activities or the universality of assets will be  automatically transferred as a whole under one of the specific procedures in the BCCA. Even  unknown debt can also be transferred automatically, but the following cannot: intuitu personae  contracts and particular types of assets such as real estate, permits and intellectual property. A  transfer of these types of assets requires certain formalities to be completed. Furthermore, asset  deals must comply with a specific procedure that entails reporting, which requires time.

If parties decide not to follow a BCCA corporate procedure for the transfer, the transfer of assets  will then have to take place ut singuli in accordance with the Civil Code. This requires every asset  to be transferred individually, so an exhaustive list must be drawn up of all assets, rights, and  obligations that are to be transferred. This list is typically included in the sale and purchase  agreement. Any item that is not mentioned on the list is considered not to be part of the assets that  will be transferred.

2.2.2 Common factors that influence each structure type

Belgian M&A transactions are generally structured as an asset deal or a share deal. Below are  some of the most common factors that influence the decision on the deal structure type.

Complexity level

Share deals are less complex. In this type of deal, the target itself continues to own all its assets and  liabilities after the transaction; only the control changes because the buyer merely acquires the  shares of the target.

Transfer formalities

Share deals have fewer formalities than those required of an asset deal. The legal rules governing  asset transfers in principle apply to every individually transferred asset (a transfer ut singuli ). In  addition, the requirements for the transfer of each individual asset that bind third parties must be  complied with. However, if the assets are transferred ut universali under the BCCA procedure,  the transferee becomes the legal successor of all those assets. This means the transferee takes over  all the rights and obligations of the target (or the rights and obligations of the universality of goods  or complete branch of activity) without the need to follow the rules of ordinary law on binding  third parties, subject to those related to intellectual property or real estate.

Protection under the Civil Code

The Civil Code protects the transferee-buyer from hidden defects and grants it the right to  undisturbed possession and enjoyment of its property. A buyer can automatically seek remedy  from the seller if the transferred assets contain any hidden defects. For the claim to be admissible,  the buyer must prove that the defect prevents or restricts its use of the transferred/sold asset in  such a way that – had it not been for those defects – the buyer would not have purchased that  asset or would have paid less for it. The law does not require the seller to be aware of these hidden  defects. Secondly, because the buyer is entitled to undisturbed enjoyment of its property, the seller  may not do anything that can cause the transferred asset to depreciate or deteriorate. The seller is  therefore bound by a de facto non-competition clause; any competition in which the seller  participates would prejudice the buyer’s right to undisturbed possession and enjoyment of the  purchased asset. In a share deal, the Civil Code does not bind the seller to any non-competition  obligation. Parties should therefore include a non-competition clause in the share purchase  agreement so that it binds the seller.

Cherry-picking of assets and liabilities    For buyers that are not interested in all the activities of the target, an asset deal is more appropriate  because the buyer can choose the activities or assets and liabilities that it prefers, whereas a share  deal implies the purchase of all the target's assets and liabilities.    Restrictions on share transfers    The target's articles of association could restrict share transfers. Please see section 1.2.1.  Consequently, parties might opt for an asset deal instead of a share deal to avoid these restrictions.

Acquisition finance    For share deals, the Belgian rules on financial aid limit the financing of share transfers. Because  these rules do not apply to a sale of assets, buyers considering a share deal should consider this  when deciding which type of deal structure it should use for the transaction.    Non-assignment clauses    Contracts that contain a clause prohibiting any assignment cannot be transferred to the buyer if  the parties to the contract concerned do not approve of the transfer. This could be an obstacle in  an asset deal. If the asset transfer is conducted according to a BCCA procedure (eg, a transfer of a  branch of activity), then in principle all contracts become transferred automatically by operation  of law (with some exceptions). In a share deal, however, the contract will not be transferred to a  third party in any event because the target continues to be a part to the contract.    Change of control clauses    Contracts with a change of control clause requiring the contracting party’s prior approval of the  transaction can be an obstacle in a share deal because obtaining consent takes time. This is less  of an issue for an asset deal: in principle, there will be no change of control over the target.    Minority shareholders    Buyers that are contemplating acquiring the entire business of the target can be confronted by  certain minority shareholders who refuse to sell their shares. In such scenario, the buyer could opt  for an asset deal: this type of transaction, in principle, requires the decision of the target's board of  directors (which is controlled by the majority shareholders). Even so, this does not eliminate the

risk that the refusing minority shareholders could sue the majority for abuse of majority position.

Tax aspects    There are different tax implications for each transaction type. See section 2.4 for more on these.    Joint and several liability

Liabilities for income tax, VAT and social security in a transfer by way of an asset deal are  effective and enforceable only after one month from the date a certified copy of the asset purchase  agreement has been submitted to the relevant authorities. In addition, the buyer will be jointly  liable for any outstanding income tax, VAT and social security liabilities, the sum of which could  reach up to the purchase price that the buyer would have to pay (or up to the debt that would be  transferred to the purchaser) before the end of the abovementioned period. A buyer can be exempt  from these liabilities if valid certificates, which are issued by the relevant authorities, stating that  the seller does not have any outstanding income tax, VAT and social security liabilities, are  attached to the submitted asset purchase agreement. These certificates may not be older than 30  days from the date of the submission.

2.3  Typical documentation for each structure

Parties enter into a share purchase agreement in a share transfer. If a company must issue new  shares to an investor, then parties sign an investment agreement as well as a shareholders’  agreement, which governs the relationship among all shareholders, including the new ones.

In an asset transfer, parties will enter into an asset purchase agreement. If assets are transferred  under a BCCA procedure, then additional documents will be required, depending on the procedure  used and the assets concerned. These documents can include a report drawn up by the board of  directors and a notarial deed.

The two agreements (one for share purchase and the other for asset purchase) have their own  indemnification mechanism. In general, the indemnification mechanism under an asset purchase  agreement, ie, the representations and warranties (R&W) and the specific indemnities are less  elaborate because the Civil Code already provides the buyer of assets with a certain level of  protection (see section 2.2.2 below). In a share purchase agreement, the wording is more  straightforward because there is no need to identify and describe each individual asset that will be  transferred.

Signing of ancillary documents is required for either transaction type. They include transitional  services agreements, licence agreements, management agreements, and so forth.

2.4  Tax aspects of M&A deals

The main tax aspects of share deals and asset deals are stipulated in the Belgian Income Tax Code.

2.4.1 Share deal

Income tax – personal

Capital gains ( meerwaarde/plus value ) on shares realised by natural persons within the normal  management of private assets are exempt from Belgian income tax. If they are realised outside of  the normal management of private assets (eg, speculative), they are taxed at a rate of 33 per cent.

Capital gains realised by a natural person in the transfer of significant shareholdings to a foreign  company (ie, a company outside the European Economic Area), are taxed at a rate of 16.5 per  cent. This rate applies only to the personal income tax scheme and is subject to the following  conditions: (1) the transferor must have owned directly or indirectly, alone or with their family, at  any time over a five-year period before the transfer, more than 25 per cent of the rights in the  company whose shares are transferred; (2) the transferee is a non-resident legal entity that does  not have its registered office, principal place of business, or place of management or  administration in the European Economic Area. If the transferee on its turn transfers within one  year the shares to a legal entity not established in the European Economic Area, the capital gain  realised on the initial transfer is taxed at 16.5 per cent in the hands of the original transferor. To  avoid this, a specific non-alienation clause relating to the resale of the shares for the concerned  period is often added to the share transfer agreement.

Income tax – corporate

Capital gains on shares are usually tax exempt if all of the following are met: (1) the company  whose shares are sold is subject to corporate taxation; (2) the seller company holds full ownership  of at least 10 per cent of the shares representing the capital of the target, or the investment value  of the participation must reach at least €2.5m; and (3) the shares have been held in full ownership  for one year without any interruption.

Value added tax (VAT)

VAT is due on the supply of goods and services and supplies that do not qualify for an exemption  under the Belgian VAT code. Share transfers are in principle not subject to VAT as they do not  qualify as either a service or a supply.

2.4.2 Asset deal

Income tax – corporate

Any capital gains realised on the assets and goodwill from an asset deal transaction will be  considered taxable profit that is subject to the normal corporate income tax rate (which was 25  per cent in 2021). Capital losses realised on assets in such type of deal are usually tax deductible.

Registration duty

Since 1 January 2022, real estate transfers are subject to a registration duty of 12 per cent (in  Flanders) and 12.5 per cent (in Brussels and Wallonia), levied on the sale price. For a transfer of  a commercial lease agreement ( handelshuur/bail commercial ), the transfer will be subject to a 0.2  per cent tax on outstanding rent and charges due under the original lease. A transfer of an  emphyteusis ( erfpacht/droit d'emphytéose ) is subject to a 2 per cent tax. No registration tax is due  if the transfer is already subject to VAT, for example, if the transaction concerns the transfer of a  new building (ie, a building less than two years old).

Value added tax (VAT)

In principle, asset transfers are subject to VAT as they fall under the definition of a supply of  goods. However, if the asset transfer relates to a universality of business or a branch of activity  ( algemeenheid van goederen of van een bedrijfsafdeling/universalité de biens ou d'une branche  d'activité ), no VAT would be due. Universality means a collection of different goods brought  together to form a whole by reason of their common use. A branch of activity is understood as a  unit that is autonomous in terms of technical and organisational aspects and can operate on its own.

There will be a transfer of a branch of activity if all the elements necessary for the operation of  the business are transferred. If this condition is not met, the general 21 per cent VAT rate will  apply to the transfer, and the buyer must pay this to the seller, which, on its turn, will have to pay  it to the authorities.

2.5  Specific compliance considerations for each transaction type

Transactions in the finance, insurance, and real estate sectors must meet specific conditions for  compliance. This M&A guide does not cover them.

See also the sections concerning the requirement for merger and antitrust clearance (section 6.2.1)  and FDI screening (section 1.2.6).

Privacy and General Data Protection Regulation (GDPR) concerns are relevant in all types of  transactions, but these require specific attention in asset deals.

3.  PRE-AGREEMENT DOCUMENTATION

3.1  Pros and cons of having pre-agreement documentation for each transaction type

3.1.1 General

During pre-contractual negotiations, parties usually draw up preliminary documents such as a  non-disclosure agreement (NDA) ( vertrouwelijkheidsovereenkomst/accord de confidentialité ) or  a (binding or non-binding) letter of intent (LOI) ( intentiebrief/lettre d'intention ) or both. For an  auction sale in particular, the process is slightly different. It starts with the distribution of an  information memorandum to potential bidders and the signing of an NDA at the same time.  Afterwards, non-binding bids are called, and bidders eligible for the next round will be selected.  Those selected will usually be allowed to conduct a due diligence investigation of the target. In  larger transactions, the due diligence can be facilitated by a vendor due diligence report. At the  end of the due diligence stage, bidders will be requested to submit binding bids, together with  mark-ups of the sale purchase agreement. The seller will then choose one or more bidders from  these bids, who will proceed to the negotiations stage. The negotiations continue until only one  bidder remains and the final transaction documentation with that bidder is signed. Parties can  enter into so-called clean team agreements (CTA) if target and buyer are competitors. In addition,  agreements governing data room access have also become more common.

3.1.2 Non-disclosure agreements

Parties usually sign an NDA at the start of the negotiations. The duration of the non-disclosure  obligation is typically two years. The NDA aims to protect the confidentiality of the negotiations  and all information exchanged between the parties. Under Belgian law, not having an NDA in place  or an explicit confidentiality clause in another agreement does not mean that the discloser of the  confidential information is not protected. A judge can order the receiver of the information to be  bound by confidentiality, although the exact scope of such confidentiality obligation is unclear.  Furthermore, the NDA can also contain exclusivity and non-solicitation clauses. The NDA is more  effective if it contains a liquidated damages clause ( schadebeding/clause pénale ).    Belgian law allows liquidated damages if the amount of the liquidated damages does not exceed  the damage that was potentially foreseeable at the time when the parties agreed upon the liquidated  damages clause. However, in the early stages of negotiations, such liquidated damages are rather

uncommon. Without such clause, it will often be difficult for the seller to establish the value of  the damage if a breach of confidentiality does occur.

3.1.3 Letter of intent

Signing an LOI before a sale and purchase agreement is common practice. Parties usually wish to  set out in this document their understanding of certain basic elements of the transaction before  they proceed to the due diligence phase and negotiate the terms of the sale and purchase  agreement. An LOI is also called a term sheet, memorandum of understanding (MOU), pre-offer,  indicative offer or heads of agreement. The structure of these documents vary in many ways, with  some letter of intents being remarkably short and simple, while others can be rather lengthy.

LOIs should be drafted with utmost care and precision because an agreement between parties  under Belgian law constitutes a binding commitment if the parties agree on the essential and  substantial elements of the transaction. These elements differ based on:

(a)  the type of transaction or contract, assessed objectively (for example, for a purchase of  goods, the consensus reached between parties is considered binding if they agree on the  subject matter of the transaction and its price, whereas for a share subscription, the essential  elements would be the number of shares and the amount of the investment); and  (b)  what the parties themselves consider to be a substantial element of the specific transaction.  (That is, what the parties consider to be the determining factor that will influence their  consent to the transaction (assessed subjectively), even though this would not be essential  from an objective point of view. Because these essential elements are subjective in nature,  they can be considered substantial only if they have been clearly communicated as such  during the pre-contractual negotiations.)

On assessing whether an LOI is binding or non-binding, the contents of the letter will prevail over  the form of the document, regardless of any disclaimers stating the contrary, its name or how the  parties categorise it. Typically, non-binding LOIs indicate only a price range instead of a fixed  price, and they make the transaction subject to several assumptions and conditions.

LOIs should reflect the intention of the parties especially in respect of their binding nature.  Ultimately, a judge will find whether a letter of intent is binding or not based on the wording of  it, other communications between the parties, and even their subsequent behaviour.

3.2  Binding nature of clauses in the pre-contractual documentation

The recitals of NDAs and LOIs often indicate which clauses are binding and which ones are not.  In practice, any clauses on confidentiality (type of information, term of confidentiality), non- solicitation and non-compete, liquidated damages, costs, exclusivity, applicable law and  jurisdiction are in principle declared to be binding from the outset, despite the non-binding nature  of the other clauses and sections of those documents. In addition, clauses on compliance with the  GDPR and on privacy, which have become common in NDAs and LOIs, are also binding.

4.  DUE DILIGENCE STAGE

4.1  Points of attention

In a Belgian M&A transaction, parties must act in a diligent manner regarding the initiative, the  continuation and the termination of the negotiations. Failure to do so could potentially give rise

to liability for a pre-contractual fault. This section explains some key aspects of the due diligence  stage

4.1.1 Parties must act diligently

Belgian law requires parties to act diligently – ie, as a normal and reasonable person would do in  the same circumstances. Even if a party is engaged in non-binding discussions, the negotiating  party must consider the interests of the other party.

Depending on whether the parties have entered into a contract, the defaulting party can be held  liable for having committed a culpa in contrahendo or a culpa in non contrahendo under general  tort law. As a general rule, the defaulting party could be ordered to indemnify the injured party so  that the latter’s position is restored as if the wrongful act had not occurred.

It is generally accepted that the indemnification should cover the so-called negative interest of  contract, such as the costs that were incurred for negotiations, the time lost and the impossibility  to seize other opportunities. Whether the injured party could successfully bring a claim for any  (additional) compensation for having lost the positive interest of contract – ie, compensation for  lost profits because of the absence of contract – has been subject of debate in jurisprudence. Book  5 of the New Civil Code recognises that, in exceptional circumstances, the positive interest of  contract is eligible for compensation if there was a legitimate expectation that an agreement would  definitely be concluded.

The party alleging that it has suffered loss must also prove its loss and the causal link between the  loss and the wrongful act. The court assesses on a case-by-case basis whether a party has  committed a wrongful act by terminating the negotiations depending on the behaviour of both  parties, the length of the negotiations and the costs involved.

4.1.2 Right to information

Currently, Belgian law does not explicitly impose an obligation on a seller to disclose information  about the target to the purchaser during the pre-contractual phase. Article 5.16 of the draft Book  5 of the New Civil Code however requires parties to provide each other, during pre-contractual  phase, with the information required by law, by good faith and custom, given the capacity of the  parties, their reasonable expectations and the specific subject matter of the contract. Parties can  of course agree in an NDA or LOI on what kinds of information about the target that the seller  must share. The fact that there is currently no specific legal provision imposing an obligation to  disclose information does not mean there is no obligation to disclose information about the target.  Considering the general legal principles and developments in case law, the matter is much more  nuanced. For example, there is a general obligation for all parties to act in a prudent and diligent  manner, also during negotiations in the pre-contractual phase. Moreover, there is an obligation to  provide essential information to one another so that the other party's consent to enter into the  agreement is not vitiated (eg, by error, fraud or duress).

Furthermore, certain sector-specific rules can also impose an obligation to disclose information.  For example, in a deal (commercial partnership) that involves the transfer of know-how, the party  granting the right to use the know-how must provide certain information to the other party at least  one month prior to the signing of the agreement.

4.2  Typical issues in a Belgian M&A transaction – an overview

The areas of focus in a due diligence investigation vary from project to project, but they will  generally include corporate, tax, labour, commercial, litigation, real estate, environment and  regulatory matters. Depending on the findings from the due diligence, the parties will negotiate  CPs and specific indemnities, and stipulate specific representations and warranties. According to  M&A surveys, indemnities across deal value typically relate to tax (67 per cent of all indemnities  included a tax indemnity). Other common indemnities relate to labour (32 per cent), litigation (29  per cent), existing agreements (25 per cent) and environment (24 per cent).

The specific indemnities are generally governed by a separate liability system that is, unlike the  representations and warranties, not subject to the same liability cap and other limitations.

Before the pandemic, the buyer usually conducted a standard due diligence on the target and its  business. Now, we see that the buyer is more preoccupied with the target’s business as a whole  and the target’s capacity to react to uncommon and highly disruptive events. For example, the  buyer will examine the agility of the business to scale downwards and upwards, supply chain  integrity, the ability to adjust and change suppliers, and the robustness and integrity of IT systems.  This means that the buyer’s due diligence checklist needs to be broad enough to leave no stone  unturned. The seller must be prepared to give appropriate answers or justifications to the buyer.

##### 5.  MAIN ACQUISITION AGREEMENTS

5.1  Formal requirements

The form and contents of the sale and purchase agreement will vary depending on the transaction  type and on the transaction-specific circumstances. A share purchase agreement (SPA) governs a  transfer of existing shares; a subscription agreement a subscription to new shares; and an asset  purchase agreement (APA) an asset transfer. One agreement can govern all these transactions.

For example, a transfer of assets ut universali , a merger or a transfer of a branch of activity will  require a specific proposal drawn up by the company’s board of directors and shareholders’  approval in an authentic deed, respectively. A valid agreement under Belgian law must have four  elements: the consent of the parties to be bound under it ( wil/volonté ), their capacity under law  ( bekwaamheid/capacité ) to enter into the agreement, a precise object ( voorwerp/objet ), and a  lawful cause ( oorzaak/cause ). The parties’ agreement does not have to be in writing, as in Belgium  the theory of consensualism applies. Therefore, parties should refrain from agreeing on a price  and an object because these constitute the elements that are essential for the formation of a binding  agreement (see section 3.1.3).

In practice, the SPA will stipulate that share ownership in a company will be transferred to the  buyer upon signing of the SPA, or upon closing if these two events are not simultaneous. The  share transfer will bind third parties (including the target) once the share transfer has been  recorded in the target's share register. Besides this, there are no other formalities for share  transfers. Asset ownership in principle will transfer when there is a valid agreement on it (and  subject to the fulfilment of additional transfer formalities for certain assets, such as real estate and  intellectual property).

5.2  Typical clauses in the acquisition agreement

A typical acquisition agreement will have the following sections and clauses.

5.2.1 Preamble

The preamble of an acquisition agreement is the introductory section that essentially provides a  background on the transaction, identifies the target and explains the interconnection of the  document with any other transaction agreements. From the seller's perspective, the preamble,  which is followed by paragraphs known as recitals, can also indicate that a due diligence has been  performed by the buyer and its advisers. Parties should state in the recitals that nothing in the  agreement should be interpreted against a party because it was responsible for drafting it. Parties  should also add that they consider that the draft does not create an economic imbalance between  them, given the new B2B legislation (see section 1.2.4).

5.2.2 Definitions

Definitions are typically the first or second section in any acquisition agreement. It is a list of the  defined terms used throughout the agreement.

5.2.3 Object clause

As stated above regarding the formation of a contract, the object of the sale or purchase must be  clearly defined. There is no sale if the parties have not agreed on the object of the transfer.

The object of a share deal is straightforward: the seller’s shares are the object, and they will be  transferred with all related rights. Parties should set out in the agreement how the dividend  distributions for the ongoing financial year and/or any outstanding dividend payments for  previous financial years should be allocated between the seller and the buyer. The agreement  should also indicate whether the shares are transferred free of any liens and encumbrances.

Drafting an object clause is more complex in an asset deal. Generally, a separate schedule  describing the object, ie, the assets and liabilities that will be transferred and/or the assets and  liabilities that are explicitly excluded from the scope of the transaction, form an integral part of  the agreement. It should be mentioned in that schedule whether the assets are transferred free of  any liens and encumbrances.    5.2.4 Purchase price

General

A valid purchase price under Belgian law must or can be determined based on objective elements  that are outside the scope of the parties’ will. Therefore, all components of the purchase price  should be clearly defined in the agreement. For example, if an earn-out mechanism applies, the  price-setting should be rigorously described, especially when considering potential future  conflicts of interests between the parties after the transfer of ownership. Similarly, payment  conditions (including the terms, conditions, amount, bank account receiving the payment, payer,  and beneficiary) should be clearly stated.

In two-step transactions (ie, when signing and closing take place at different times), and subject  to the locked box mechanism currently applied, it is common practice to include a price  adjustment mechanism, following which the purchase price will be adjusted higher or lower based

on certain financial factors (net debt, cash, etc.) at closing. Parties would usually go through tough  negotiations to come up with a clearly defined calculation procedure and different components of  such mechanism that they agree on.

It is common to include a clause requiring a third-party expert to come up with the final calculation  and method if the parties' disagreement on this persists. Such a clause is valid if the third-party  expert accepts the instruction, and if the agreement contains objective calculation components  that enable the third-party expert to complete their task.

Depending on the seller’s financial situation – thus, the likelihood that a seller can indemnify  the buyer in the event of breach – a buyer can demand the seller to agree on certain protection  mechanisms by using part of the purchase price to this effect. In practice, this is required only  if certain risks have been identified after the due diligence investigation. Contrary to the French  law system of garantie de garantie , this is not standard practice in Belgium. There are several  mechanisms for this, each with their own advantages and drawbacks.    Escrow account  An escrow account is a blocked special purpose bank account that holds a part of the paid purchase  price for a certain period of time. This bank account is contractually stipulated and agreed upon  (for example, the time period during which the buyer can bring a claim for breaches of the  representations and warranties). The parties could agree on a reduction of the blocked amount,  for example, on each anniversary date of the transfer.

The escrow account can be held in the name of the seller, the buyer, or both jointly. More  importantly, parties should clearly stipulate that the interest gained on the balance of this account  will accrue to the party who is entitled to the escrow amount and how the procedure for releasing  the amount should be handled. This procedure should be detailed in an escrow agreement, which  is also signed by the escrow bank, and whose clauses are aligned closely with the clauses of the  acquisition agreement. In this respect, the escrow agreement should explicitly state that all its  provisions prevail over any conflicting provisions in the bank’s general terms and conditions.  Contrary to the system under English common law, where the escrow concept originated, an  escrow account may not be enforced under Belgian law against other creditors if concurrent rights  exist, ie, when the account holder is in a state of insolvency.

An alternative to this could be to open a bank account in the seller’s name and to pledge the  potential claims towards the seller in favour of the buyer.

A bank guarantee entails a similar technique: the seller is the one who receives the entire purchase  price at closing, and the seller – through the bank – provides security to the buyer.

The bank guarantee can be subject to several conditions. The bank could also demand that the  seller block a certain sum in a bank account held at the same bank (but this effectively defeats the  greatest advantage of the guarantee mechanism). Depending on the acquisition agreement, the  guarantee can be payable on first demand or upon presentation of certain documents by the buyer.

Alternatively, a third party (for example, the seller’s parent company) could be the one providing  the guarantee to secure the seller’s obligations under the acquisition agreement, including those  with respect to the representations and warranties made and breaches of them. From a buyer-side  perspective, it is advisable to include a clause stating that the seller and guarantor are jointly and  severally liable for these obligations.

Deferred payment

A deferred payment means that the buyer pays a certain percentage of the purchase price at a later  point in time. Before then, it has the right to withhold this amount and use it to set off any  indemnification payments that the seller would owe under the acquisition agreement.

This deferred payment mechanism is different to the other two in that the buyer’s ability to  withhold a certain amount of the purchase price enables it to decrease its risk exposure if the seller  becomes insolvent, although in principle, any set-off of claims is not allowed in the event of  insolvency (with certain limited exceptions).

Additionally, the buyer could also have insufficient financial resources to pay the full sum at  closing. Therefore, it is not uncommon for the seller to demand a bank guarantee from the buyer  for the deferred payment.

A deferred payment mechanism can also be combined with a vendor loan (subordinated or not)  and corresponding security as collateral. In other words, it can be used as a financing mechanism  whereby the parties agree on methods to secure repayment, which will essentially comprise a set- off possibility and the granting of pledges.

5.2.5 Representations and warranties

As stated above, buyers, especially in share deals, have limited protection under Belgian law.  Therefore, buyers would usually have the acquisition agreement, especially SPAs, stipulate  tailored and specific contractual representations and warranties (R&Ws). Sellers must state that  the R&Ws are true, complete, accurate and not misleading. Belgian law offers a significant level  of flexibility in this respect, and there are various ways available to the seller that can limit its  liability.

General considerations    Typical R&Ws relate to the following, which are by no means exhaustive: the target's business,  its shares, financial statements, real estate and movable assets, litigations, personnel, tax issues,  environmental issues, permits and subsidies, intellectual property rights, key contracts, intragroup  arrangements, arrangements with shareholders and directors, and so on. How these clauses are  drafted and the words and language used are very important, as courts usually interpret them  restrictively.    In two-step transactions, the buyer should demand the seller to repeat the R&Ws at closing and  thus confirm that they are again true, complete, accurate and not misleading – not only at the time  of signing but also up to and including closing. The pandemic has caused parties to rethink the  bringing down of the R&W at closing.    For some specific transactions, such as secondary buy-outs and management buy-outs, it is not  uncommon in Belgium to have a very limited set of R&Ws. This is because the buyer (which is  the management members) has sufficient and thorough knowledge of the target and its business.    For transactions involving the subscription of new shares, the company concerned is the party  giving the R&Ws. This is a somewhat ambiguous situation because the buyer, who is the  shareholder of the company, will have to financially contribute to indemnifying itself.

R&W limitations    The format and scope of the disclosures against R&Ws can vary. This causes parties to have  diametrically opposed preferences and undergo tough negotiations. Parties can agree to have the  entire data room disclosed, which contains due diligence information made available to the  potential buyer. Unlike in the United States, this type of disclosure is rather common – especially  in the current landscape of the seller’s market. Parties can also choose to sign a separate disclosure  letter in which the seller declares that it is aware of specific issues.    In any event, the seller should carefully analyse the target and provide the buyer with essential  information that enables it to make a well-considered decision. Sellers often try to have the buyer  acknowledge that it has undertaken a due diligence investigation. Although the actual effect of  this acknowledgement is limited, it could still be used in court or arbitration proceedings. On the  other hand, buyers should try to have the seller acknowledge that the R&Ws have had a conclusive  effect on the buyer’s decision to purchase the shares or assets.    R&Ws play an essential role in indemnifying the buyer. They therefore act as an incentive for the  seller whereby the more potential risks that it discloses, the more it is covered before closing  because the liability will shift to the buyer, subject to the extent these disclosures are accepted by  the buyer.    Disclosures against R&Ws certainly have an impact on price discussions. They are even grounds  for a price reduction at times. If the seller does not agree to reduce the price and the buyer refuses  to accept any liability, the seller remains obliged to indemnify the buyer for any harm or loss it  would incur if any of the R&Ws is incomplete, inaccurate, or misleading. If this occurs, the  disclosure concerned can be neutralised by adding a specific indemnity to cover the particular  risk in question.

R&Ws can be qualified at the level of ‘the best knowledge of the seller’, or a similar expression.  This allows for the R&Ws to exclude facts and circumstances that the seller, acting in good faith,  could not have known from the scope of the R&Ws. The extent of this limitation depends mainly  on how this phrase is defined, which is usually a point of discussion during negotiations. From a  seller-side perspective, it should make the R&Ws only based on the facts that certain identifiable  people have actual knowledge of on or before the date of the agreement. From the buyer’s side, it  should try to set the scope of the R&Ws to be as wide as possible, and include the knowledge of  not only the seller but also that of any director, executive or even employee of the target. In  addition, the buyer should include a reference to reasonable knowledge. This kind of knowledge  implies that those particular individuals are considered to have knowledge of any fact that a  reasonably diligent person who is placed in the same circumstances could be expected to discover  during a reasonably comprehensive investigation concerning the existence of such fact. In  practice, this often leads to disputes between parties and an onerous burden of proof on the one  relying on it.

5.2.6 Indemnification

General

A clearly worded indemnification clause is necessary in agreements governed by Belgian law.  This type of clause essentially stipulates that the seller agrees to indemnify the buyer to restore  the latter’s position to what it would have been had it not incurred any harm or loss. When it  comes to defining the notion of harm and loss and to restricting payment of indemnification, this  will depend mainly on the parties’ negotiating positions and on the outcome of the due diligence.

In principle, only the buyer can seek indemnification for harm or loss suffered. However, the  parties can agree that the indemnification mechanism can also benefit the company itself, whereby  the company could also be entitled to seek indemnification. This could be useful in relation to  taxation considerations.

Limits to indemnification

A seller's liability under an acquisition agreement can be subject to the following limitations.  They do not apply if the seller is guilty of fraud.

De minimis

-  Limit to each individual claim: there will be no warranty for claims below a certain value; or  •  Limit to an aggregate of claims: the claimant is allowed to make a claim if a certain value (ie,  a ‘basket’ of claims) has been reached. If so, and depending on the negotiation position of the  seller, the buyer will usually be indemnified for the entire claim and not only for the threshold  excess.

Cap

The seller’s liability can be capped at a certain value, which is the total sum of the claims. The  seller will not be liable for claim values exceeding the cap. Parties usually set the cap as a certain  percentage of the purchase price. The cap can also decrease through time to the extent there have  been no claims.

Duration

Acquisition agreements should set a time limit for claims, after which the claims are inadmissible.  The time limit in practice is usually between 18 months and three years. For certain types of  liabilities, such as tax and social security and sometimes environmental liabilities, the duration  usually coincides with the statute of limitations, after which the respective public authorities  would no longer be able to claim the sums for events before the transaction. Regarding  indemnification pertaining to share ownership, parties usually stipulate a 30-year period, which  corresponds to what is set in the statute of limitations for such type of claim.

Seller protections

Acquisition agreements can provide for a range of different mechanisms that protect the seller. It  is common for Belgian acquisition agreements to include provisions that neutralise any potential  effects of taxation. Similarly, parties can also contractually set out the details on how to manage  third-party claims and defence conduct. Parties can also agree that a seller cannot be held liable  for any harm or loss that has been caused by a change of law.    Finally, despite the fact that R&W insurance was rare in the Belgian M&A market for many years,  there has been an increase in R&W insurance, especially in auctions in which the seller imposes  R&W insurance as a condition to the bidding process.

5.2.7 Conditions of closing

See section 6.1.

5.2.8 Closing

See section 7.1.

5.2.9 Buyer and seller covenants

Pre-closing

During the period between signing and closing, parties will generally agree on a standstill clause.  This requires the seller to conduct the company’s business only in the ordinary course and to  preserve it as a going concern. The seller is therefore prohibited from performing certain acts:  these typically include declaring dividends, amending the articles of association, granting  securities and incurring more debt (other than those that are required for the ordinary course of  business).

Furthermore, the seller must fully pay off before closing all the debt that it owes to the company.

The pandemic and related uncertainties have caused buyers to want more control over the business  between the time of signing and closing. In view of competition law compliance, parties should  manage gun-jumping risks and reassure buyers through other ways during this interim period.

Post-closing

In many deals, the directors of the target company are also its shareholders, or they at least have  some connection with them. The acquisition agreement should include a clause on the discharge  of directors’ liabilities. This discharge could be granted at first at the time of the closing.  Subsequently, the shareholders will have to discharge the directors from their liability at the next  annual shareholders’ meeting. Usually, the directors concerned would resign on closing. The  seller should require that the buyer undertake to discharge these directors from performing their  mandate until closing.

Parties can include certain covenants regarding earn-out payments whereby the buyer in essence  agrees to conduct the business in the same manner as before the transaction. In addition, the  acquisition agreement can provide for some mechanisms to ensure that the seller continues to  monitor certain developments, for example, by having an observer on the board of directors, and  by having the buyer fulfil reporting obligations.

It is typical in practice to stipulate in the acquisition agreement that the seller undertakes to:

(a)  not compete with the company or the business sold;  (b)  not disclose or use confidential information concerning the business acquired;  (c)  not solicit employees, suppliers, or customers, and  (d)  not interfere with the business or impair its goodwill in any other way.

A valid non-competition restriction under Belgian law must be limited in time, territory and scope  of activities. This clause should be tailored to ensure that the buyer can effectively benefit from  the goodwill of the business it has purchased. For example, the validity period must be limited to  the time necessary to bind the transferred clients.

If one of the above limitations is not stipulated, a court will hold the restriction invalid. A court  will thus not simply reduce the clause to what is reasonably acceptable and permitted under  Belgian law unless the agreement contains a severability provision. Given the rather heavy burden  in proving actual harm or loss from a contractual breach, it is common practice to provide for a

lump sum indemnification in the event of breach. A clause providing for this could be qualified  as a penalty clause. A court will then assess whether the harm or loss suffered corresponds to the  harm or loss that was actually foreseeable at the time of signing the contract. Belgian law confers  power on the court to reduce the contractually stipulated penalty if the sum is considered to be  obviously unjustified. Specific language could be used to reduce the risk of qualifying the clause  as a penalty clause.

Finally, and for transactions involving a seller who is a natural person, appropriate language  should be used in drafting the acquisition agreement to avoid the 16.5 per cent capital gains tax on  a sale of shares belonging to a substantial shareholding in a Belgian company. Acquisition  agreements often impose an obligation on the buyer to not sell or transfer the shares to any  company outside the EU for 12 months after closing.

5.2.10 Boiler-plate provisions

Most agreements have standard clauses (eg, clauses on severability, entire agreement,  confidentiality, notices, assignment, costs, governing law, etc.). Just because they typically appear  does not mean they are any less important.

5.2.11 Signature

See section 1.2.5.    5.3  Dispute resolution mechanism

Parties can resort to the ordinary courts and arbitration if disputes arise between them. The most  common arbitral institution designated to settle disputes from Belgian sale and purchase  agreements is either the Brussels-based CEPANI ( Belgisch centrum voor arbitrage en mediatie –  Centre belge d’Arbitrage et Médiation ) or the Paris-based International Chamber of Commerce,  which is part of the International Court of Arbitration. According to the findings from a recent  M&A survey, 78 per cent of the parties who decide to resort to arbitration choose CEPANI as the  arbitration institution that has jurisdiction over their disputes.

The dispute resolution or forum clause must be carefully drafted so that it will not give rise to a  dispute. The choice of forum chosen (ie, whether a court or arbitration tribunal) will depend on  several factors, which are explained below.

5.3.1 Length of the proceedings

The average duration of arbitration proceedings at CEPANI is between nine and ten months. For  disputes concerning a small financial value (eg, less than €12,500), proceedings last less than four  months. The duration of the proceedings starts at the time the application for arbitration is  launched (ie, when the arbitrators are appointed) and lasts until the time a final arbitral award is  rendered. The preliminary stage regarding the appointment of the arbitrators can take some time,  however, given that the disputants should agree on the appointments. Choosing three arbitrators  can reduce disagreements since each party will appoint one arbitrator of its own choice, and those  two arbitrators will jointly appoint the third arbitrator.

The rapid pace of arbitration proceedings can be explained by the fact that an arbitral award is  final and not subject to appeal (unless one party petitions an ordinary court to have an arbitral  award set aside, which is only possible in limited circumstances), among other reasons. An  arbitration clause does not prevent the parties from being able to seek urgent interim measures in

summary proceedings before the ordinary courts.

Because the Belgian courts are severely backlogged, ordinary court proceedings take much longer  before a final judgment is rendered. In addition, a party can appeal against a judgment, which  prolongs the litigation even more. In Brussels, for example, the waiting period between requesting  a hearing date for appeal proceedings and the hearing itself can be up to two years.

5.3.2 Costs

The costs for arbitration proceedings at CEPANI include the fees and expenses of the arbitrators  and the tribunal's administrative expenses. The costs are set according to a scale, which is based  on the value in dispute. The arbitrators pronounce in the final award the arbitration costs, and it  decides which party (claimant or respondent) must bear them or in what proportion they should  be paid by the parties. The final nature of an arbitral award also enables parties to save some costs  (including additional lawyers’ fees).

Court proceedings are free of charge, but the losing party is usually ordered to pay specific legal  costs to the other party. This sum also depends on the value in dispute, which is laid down in the  Belgian Judicial Code.    5.3.3 Expertise of the arbitrators

Because the parties in an arbitration appoint the sole arbitrator (or three arbitrators) by themselves,  this allows them to select certain arbitrators with sector-specific expertise.

In a lawsuit, the case could be allocated to a judge who does not have any expertise in the target’s  sector (or even in cross-border acquisitions). When this occurs, experts have to be appointed to  give their opinion.

5.3.4 Confidentiality

Contrary to lawsuits, which are conducted in a hearing that is open to the public, arbitration is in  principle confidential. The arbitral award is published only if the parties allow it, whereas any  third party with standing can request a copy of a judgment from the court's clerk.

5.3.5 International aspect

In international transactions with parties from different jurisdictions, it is customary for them to  elect for arbitration instead of bringing the dispute before court. This maintains the balance  between the parties and eliminates the advantage that one of the parties has if it originates from  the same place as the selected forum.

Arbitration clauses are being featured increasingly in acquisition agreements because of their  deterrent nature because of the high costs involved.

##### 6.  TYPICAL CLOSING CONDITIONS AND RELEVANT REGULATORY SYSTEM

6.1  Typical closing conditions

6.1.1 General

Although it is in theory possible to have signing and closing take place at the same time, most

transactions follow a two-step approach whereby they sign first and then several CPs must be  fulfilled after signing. Only after these are fulfilled will the buyer pay the purchase price and  ownership be transferred. When this is completed, it becomes the closing of the transaction.

If any of the CPs are not fulfilled, and if none of the parties exercises its right to waive fulfilment  of the CPs, which is granted in the agreement closing will not occur. 12 It is common to stipulate  that, in these circumstances, the agreement terminates or that one of the parties is entitled to  terminate the agreement. Furthermore, it is very common to provide in the acquisition agreement  that the fulfilment of the CPs does not have retroactive effect.

Parties should pay particular attention to the validity of the CPs. Belgian law requires that CPs relate  to a future and uncertain event, and this event must be incidental and external. Incidental means  that the condition cannot relate to the elements required for the formation of a valid agreement.  For example, a director of a company must not sign an agreement that is conditional on the  approval of it by the board of directors of the same company. External means that the condition  must lie outside the contractual obligations or undertakings of the purchaser and the seller. An  example of a non-external condition is a clause that states that the seller will sell the shares under  the condition that the purchaser pays the price of those shares. Furthermore, under Belgian law,  CPs whose realisation depends entirely on the will of the party that has bound itself conditionally  are null ( louter potestatieve voorwaarde/condition purement potestative ).

6.1.2 Examples from practice

A textbook example of a CP is the obtaining of the necessary antitrust approvals from the  European Commission or the Belgian Competition Authority. The period between signing and  closing usually corresponds to the time needed by the authorities to adopt a decision (whereby the  parties must perform the obligations imposed therein) or to not object to the transaction. Another  common CP is the obtaining of financing.

For asset transfers, it is common to require the seller to provide, at closing, certificates from the  authorities attesting that it has no outstanding tax liabilities, that it is not subject to any tax audit,  and that it owes no social security contributions. These certificates will be filed with the respective  authorities to avoid joint and several liability for the relevant tax liabilities.

6.2  Regulatory approvals, notifications, and the duty to inform and consult employees

Belgian M&A transactions are in theory not subject to any governmental approval or public  interest screening, but there are certain exceptions (see section 1.4).

6.2.1 Merger control and antitrust clearance

Belgian competition law has a merger control clearance system that strongly resembles the EU  competition law system.

Merger control rules apply to operations that result in a lasting change of control in an undertaking  because another company or person gains the possibility of exercising decisive influence over  strategic decisions of this undertaking (ie, a concentration). Such situations occur particularly  when two independent undertakings decide to integrate (ie, a merger), when one undertaking or  one person having control over an undertaking acquires another undertaking or part of its activities

(ie, an acquisition via a share deal or asset deal), or when two undertakings create a lasting  common undertaking between them (joint venture). The concept of concentration used in Belgian  law is the same as the concept under the European Merger Regulation, with some exceptions (for  example, operations that lead to a change of control in non-full-function joint ventures, which  could constitute a concentration under Belgian law but not under EU law).

The buyer must notify a concentration to the Belgian Competition Authority if the transaction  meets the following thresholds:

(a)  the combined turnover of the undertakings concerned in Belgium exceeds €100m;  (b)  at least two of the undertakings concerned each generate a turnover of more than €40m in  Belgium; and  (c)  the concentration does not satisfy the European Union’s merger control thresholds – this  will trigger the one-stop-shop system of notification with the European Commission.

All transactions that fall within the scope of Belgian merger control rules must be notified to the  Belgian Competition Authority before the parties are allowed to implement or proceed with the  concentration. In principle, the parties are prohibited from ‘jumping the gun’ (see section 6.1.1).

Concentrations must be notified to the Prosecution Service of the Belgian Competition Authority.  This is done by completing and filing an official notification form. The information requested in  this form is the same as those required in the CO form used by the European Commission. The  only difference is that the information relates to the Belgian market and not the European internal  market.

A peculiarity of the Belgian merger control system is that the Belgian Competition Authority  strongly relies on pre-notification talks. These are informal meetings with the Authority for the  purpose of preparing the official notification form. They last up to an average of three to four  months. The reason for these meetings is to gather the extensive information required in the  notification form, even for transactions that qualify to be done via the simplified procedure.

Once the Authority concludes that the notification form is complete, it will formally accept the  notification and, in the first phase, decide within one to two months if it is a simplified procedure  (and three to five months more if a second phase decision is needed). In Belgium, most  concentrations are approved via the simplified procedure.

Consequently, companies planning a transaction that must be notified to the Belgian Competition  Authority should be aware that the overall procedure will take around four to six months. During  this time, they will need to cooperate with the Authority by providing extensive data, and they are  prohibited from implementing the transaction.

6.2.2 Foreign direct investment screening

See section 1.2.6.

6.2.3 Specific governmental authorisations and notifications

See section 1.4.

6.2.4 Duty to inform and consult employees

This section contains an overview of the obligation to inform and consult employees under an

asset deal and share deal, including the timing and the information that should be provided to the  employees.

Asset deals

If an asset deal (either a transfer ut singuli or a transfer under a BCCA procedure) qualifies as a  transfer of undertaking within the meaning of CBA No. 32bis, then the employees must be  informed and consulted about it. Whether an asset transfer qualifies as a transfer of undertaking  within the meaning of CBA No. 32bis must always be assessed on a case-by-case basis.    Share deals

Not every share transfer will trigger the duty to inform and consult employees. A case-by-case  analysis is required in each case.

A duty to inform and consult employees, among other obligations, arises if a share transfer results  in a concentration or implies an important structural change that the company is negotiating on.  A concentration is considered to exist if the share transfer will cause the buyer of shares to acquire  control over a company that was autonomous before the sale. In such scenario, both the buyer (the  company acquiring control) and the target (the company over which the control is being obtained)  will have to fulfil the obligation to inform and consult.

Who should be informed

Who should be informed and/or consulted depends on the presence of employee representation  bodies in the company concerned.

The  employee  representation  bodies  at  national  level  are  the  Works  Council  ( Ondernemingsraad/Conseil  d’entreprise ),  the  trade  union  delegation  ( syndicale  afvaardiging/délégation syndicale ), and the Committee for Prevention and Protection at Work  ( Comité voor Preventie en Bescherming op het Werk/Comité pour la Prévention et la Protection  au Travail ). If there is no Works Council, social dialogue takes place at the level of the trade union  delegation. If neither of these exist at the company, the Committee for Prevention and Protection  at Work is the employee representation body that must be informed and consulted regarding the  transaction. 13

If there are no employee representation bodies at the company (or companies), there is no  obligation to inform and consult the individual employees about the (contemplated) transaction  unless the transaction qualifies as a transfer of undertaking within the meaning of CBA No. 32bis.

Procedure and timing

Employees have the right to be informed. This right to information means that the employer must  communicate certain information about the transaction in such a way that the employees can grasp  the socio-economic situation of the company.

The aim of consulting is to have the employee representatives and the employer engage in a  dialogue about the contemplated transaction. It is debated whether the obligation to consult  applies only if the transaction has an impact on employment or if it applies in all cases regardless  of such impact.

For transfers of undertakings, CBA No. 32bis states that, if there are no employee representative  bodies at the company, the employees must be informed individually about:

(a)  the date or intended date of the transfer;  (b)  the reason for the transfer;  (c)  the legal, economic, and social consequences of the transfer; and  (d)  the measures envisaged in relation to the employees.

For company transactions with a cross-border element, the European Works Council must be  informed and consulted in some circumstances (see section 6.2.4).    When employees should be informed and consulted

Regarding timing, the employee representative bodies must be informed before any public  announcement of a sufficiently concrete proposal for a decision on the transaction. Usually, this  is right before the parties sign the acquisition agreement. In any event, providing them with  information and consulting them must be completed before the final decision is made on the  transaction.

##### 7.  CLOSING ACTIONS

7.1  Typical steps to consummate the proposed transaction

At closing, the buyer pays the price for the shares or the assets.

In most transactions, parties sign ancillary documents or agreements at closing, such as resignation  letters of the directors, management agreements, transitional services agreements, licence  agreements, vendor loans and shareholders' agreements.

In a share deal, the share transfer will have to be recorded in the shareholders’ register at closing.  Other documents that are common in a share deal include resolutions on the appointment of new  directors, on granting temporary discharge to the exiting directors, and on the management body's  granting of daily management powers and/or specific powers to designated persons.

In an asset deal, the seller will provide a copy of the certificates confirming that the company has  no outstanding tax and social security debt (see section 6.1). For real estate transactions, the transfer  of rights in rem must be recorded in a notarial deed.

If, at closing, parties decide to undergo a capital increase, or if a BCCA corporate restructuring  procedure is carried out, they will need to appear before a notary to have these processes witnessed  and confirmed.

If there are many obligations that need to be performed at closing, parties usually sign a closing  memorandum to set out those obligations.

7.2  Points of attention in cross-border M&A deals

Regarding applicable laws, the BCCA has a legal framework for cross-border mergers  ( fusie/fusion ), demergers ( splitsing/scission ) and assimilated transactions ( gelijkgestelde  verrichtingen/operations assimilées ) only. It does not address other types of cross-border M&A  transactions defined by law, such as cross-border transfers or cross-border contributions of a

branch of activity or a universality of goods. The latter types of transactions can be performed if  they comply with private international law principles. In practice, this means that company law  ( lex societas ) applies to the rules on decision-making and legal consequences of those decisions,  and the place where the assets are located ( lex rei sitae ) governs the binding effect of the transfer.

In addition, the following aspects have an impact on the transaction closing process:

(a)  Each company must comply with the provisions and formalities that its national law  imposes on the transaction.  (b)  Consent from each participating shareholder or partner of the Belgian company is needed  if the shareholder/partner is or could become liable without limit as a result of the  transaction. Consent from them would not be required for domestic mergers and  demergers.  (c)  Contrary to a domestic merger or demerger, which becomes complete as soon as all the  companies involved have taken corresponding decisions, cross-border demergers and  mergers must fulfil additional formalities. A cross-border demerger requires a Belgian civil  notary to issue a premerger certificate in which they confirm that the company concerned  has fulfilled the required formalities under Belgian law. A similar certificate is also needed  for a cross-border merger.

Regarding employment in cross-border M&A transactions, the European Works Council will  have to be informed and consulted under certain circumstances if the transaction in question has  a transactional aspect.

##### 8.  POST-CLOSING

8.1  General post-closing actions

An excerpt of the resolutions regarding the appointment and the dismissal of directors must be  published in the Annexes to the Belgian Official State Gazette. The company's information in the  records of the Crossroads Bank for Enterprises will have to be updated as well.

Changes often take place after closing concerning the articles of association, the registered office  or the statutory auditor of the companies involved. Decisions on all these changes will need to be  filed and published in the Belgian Official State Gazette.

8.2  Regulatory filings

8.2.1 Share deal

Generally, a transfer of existing shares does not need to be registered or filed, but there are certain  deal-specific exceptions:

(a)  When the shares of a limited liability company (BV/SRL) and a public limited liability  company (NV/SA) are gathered in one hand. This gathering must be filed with the Court  of Enterprises and published in the Belgian Official State Gazette.  (b)  When there are changes to the ultimate beneficial ownership of the target company. This  must also be filed, and the management body of the target company must do this within  one month.  (c)  If the transaction concerns a subscription of new shares. In such a scenario, the notarial  deed affirming the subscription must be filed with the Court of Enterprises, and an

excerpt of the deed must be published in the Annexes to the Belgian Official State  Gazette.

8.2.2 Asset deal

Whether the transfer of a particular asset triggers the need to conduct a regulatory filing depends  on an asset-per-asset analysis. The transfer of rights in rem and leases can be subject to filing  requirements. Applying for a new permit may be required.

All asset deals that are carried out under a BCCA procedure (merger, demerger, carve-out of a  branch of activity, contribution of a branch of activity or contribution of a universality of goods)  require a notary to be involved and various filings to be made. The different reports and minutes  that are needed to complete a hybrid statutory M&A procedure must be filed with the clerk’s  office of the Court of Enterprises, and an excerpt of such documents will likely have to be  published in the Belgian Official State Gazette.

Again, as elaborated upon above, certain assets (such as real estate and IP) will still require a  separate regulatory filing.

8.3  Regulatory requirements and ongoing statutory compliance

Various ongoing regulatory requirements must be fulfilled. The most important ones are described  below.

8.3.1 General corporate

The management body must prepare the annual financial statements, inventory, and the annual  report every year. The approved financial statements must be filed with the National Bank of  Belgium 30 days after the general meeting has approved them, and in any event no later than  seven months after the end of the company’s financial year. A company’s accountant usually does  this.

The UBO register must be updated within one month if there is any change to the ultimate  beneficiary owners and their information. All UBO information must be confirmed or updated  every year.

If a company’s net asset value ( actif net/nettoactief ) falls below 50 per cent of the amount of its  capital ( capital/kapitaal ), then the management body must convene an extraordinary general  meeting within two months from the time the management body had or should have had  knowledge of the financial state of the company. The extraordinary general meeting will decide  on the continuation of the company's activities. The management body must draft a special report  containing proposed remediation measures, and it must submit this report to the extraordinary  general meeting.

8.3.2 Employment

If the company has a Works Council, this Works Council must receive certain economic and  financial information on the company every year. Further, when decisions that could have an  important impact on the company are made, information must be provided to the Works Council  from time to time without the need to wait for a meeting that is dedicated to the providing of  periodic information. This information must be given as soon as possible.
