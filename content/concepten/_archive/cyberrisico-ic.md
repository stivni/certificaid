---
title: Cyberrisico in IC-context
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.X.A
- 1.7.X
- 1.7.X.D
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/cyberrisico-ic.json
gegenereerd_op: '2026-05-21'
---
# Cyberrisico in IC-context 🔗

Cyberrisico is het risico van financiële, operationele of reputationele schade door cyber-incidenten zoals ransomware, phishing, datalekken en business interruption. Voor de internal-control-architectuur is het een specifieke risicocategorie die zowel technische (firewall, EDR, 2FA) als organisatorische (awareness, incident response) maatregelen vereist. Stagiairs herkennen dit thema bij audits van entiteiten met essentiële diensten (NIS-2) en bij AVG-meldingsplicht na datalek.

> [!summary] Korte inhoud
> Cyberrisico is het risico van financiële, operationele of reputationele schade door cyber-incidenten — ongeautoriseerde toegang, ransomware, phishing, dataverlies, business interruption.

> [!info] Behoort tot: [[geinformatiseerde-omgeving-ic]]

> [!info] Bestaat uit (1): [[nis-2-richtlijn]]

Cyberrisico is het risico van financiële, operationele of reputationele schade door cyber-incidenten — ongeautoriseerde toegang, ransomware, phishing, dataverlies, business interruption. Voor de interne controle vereist het specifieke technische en organisatorische maatregelen die de klassieke IC-componenten aanvullen.



## Bouwstenen

### Vier hoofdtypen cyberdreigingen 🤖

Ransomware (encryptie + losgeld), phishing/CEO fraud, data-exfiltratie, business email compromise (BEC).

**Waarom?** De vier types vragen verschillende controles: ransomware vereist offline backups, BEC vereist verificatie-procedures op leverancier-bankgegevens.




_Grondslag: IT-security-vakdoctrine_

### Technische maatregelen 🤖

Firewall, endpoint-detection-and-response (EDR), tweefactor-authenticatie (2FA), encryptie van data in transit en at rest, geregeld patch management.

**Waarom?** Technische verdedigingen vormen de eerste laag; 2FA alleen al sluit een groot deel van phishing-aanvallen af.




_Grondslag: Cybersecurity-vakdoctrine_

### Organisatorische maatregelen 🤖

Gebruikersbeheer (joiner-mover-leaver), awareness-training, incident response plan, offline back-ups, bevoegdheidsmatrix.

**Waarom?** Mensen zijn de zwakste schakel: een goed getraind team detecteert phishing voordat technische controles falen.




_Grondslag: Cybersecurity-vakdoctrine_

### Verificatie-procedure op leverancierbankgegevens 🤖

Bij elke wijziging van bankrekeningnummer van een leverancier wordt het nieuwe nummer telefonisch geverifieerd via een eerder bekend nummer, nooit via een nummer uit de e-mail die de wijziging aanvraagt.

**Waarom?** Business email compromise is anno 2025 de meest succesvolle fraude tegen KMO's; deze ene controle sluit het grootste deel af.




_Grondslag: Anti-BEC-doctrine_

### Reglementair kader (NIS-2 + AVG) ⚖️

NIS-2-richtlijn (EU 2022/2555, omgezet in België) verplicht middelgrote en grote ondernemingen in essentiële en belangrijke sectoren tot cyberbeveiligingsmaatregelen en meldingsplicht. AVG vereist datalek-melding aan GBA binnen 72 uur.

**Waarom?** Niet-naleving leidt tot sancties en aansprakelijkheid van de bedrijfsleiding; voor stagiair is herkenning belangrijk bij anti-witwas-controles en governance-vragen.




_Grondslag: Richtlijn EU 2022/2555 + AVG art. 33_

### Systeemuitval en verlies van audit-trail ⚖️

Twee specifieke digitale-proces-risico's naast cyberaanvallen: (1) systeemuitval — onbeschikbaarheid van het systeem door hardware-falen, ransomware, stroom-uitval of cloud-incidenten met directe gevolgen voor de financiële afsluiting; (2) verlies of manipulatie van audit-trail — logbestanden die ontbreken, overschreven worden of door admin-privileges aanpasbaar zijn, waardoor ongeautoriseerde wijzigingen onopgemerkt blijven.

**Waarom?** ISA 315 (herzien-2019) Bijlage 6 par. 2(c) eist controles op IT-activiteiten (back-up, recovery, monitoring) precies om systeemuitval op te vangen. Bijlage 6 par. 2(a) eist toegangscontroles op beheerderstoegang omdat die directe manipulatie van logs en data mogelijk maken — verlies van audit-trail betekent dat de auditor de werking van geautomatiseerde controles niet meer kan reconstrueren.


**In de praktijk**: Systeemuitval-controles: documented disaster-recovery-plan met RTO/RPO-doelen, jaarlijkse restore-test, redundantie (RAID, dubbele datacenter, cloud-availability-zones). Audit-trail-controles: write-once-logging op kritische tabellen, scheiding tussen sysadmin (beheert systeem) en security officer (reviewt logs), SIEM-tool voor alert op verdachte database-handelingen.

Bij Rotex Roeselare NV viel het ERP tijdens de jaarafsluiting 2024 zes uur uit door een storage-controller-defect. Door geteste hot-standby was de impact beperkt; zonder zou de afsluiting met dagen vertraging zijn opgelopen. 🤖
Bij Yperse Werkplaats BV bleek een bonus-uitbetaling van € 12.000 nooit door HR aangevraagd, maar wel via direct database-update verwerkt — geen log-spoor omdat de IT-administrator zowel uitvoering als log-rotatie beheerde. Functiescheiding op admin-niveau was de gemiste controle. 🤖

_Grondslag: ISA 315 (herzien-2019) Bijlage 6 par. 2(a) + 2(c)_


## In de praktijk

<h3 id="cyberrisico-is-een-risico-inschattings-input-geen-aparte-controle">Cyberrisico is een risico-inschattings-input, geen aparte controle</h3>

> [!tip]- Cyberrisico is een risico-inschattings-input, geen aparte controle
> In de COSO/ISA 315-architectuur is cyberrisico een element van risico-inschatting (component 2). De effectieve antwoorden op cyberrisico zitten in beheersactiviteiten (component 3, vooral ITGC en application controls) en monitoring (component 5). Stagiair moet dus de link leggen tussen cyber-risico-inschatting en concrete IT-controles, niet cyber als 'apart hoofdstuk' behandelen. 🤖


## Zie ook

- **Vereist kennis van**: [[avg-interne-controle]]
- **Vereist kennis van**: [[it-general-controls]]
- **Vereist kennis van**: [[risico-inschatting-organisatie]]
- **Wordt voorondersteld in** (1): [[geinformatiseerde-omgeving-ic]]
## Voorbeelden

Bij Yperse Werkplaats BV trof in 2025 een ransomware-aanval het ERP-systeem; productie lag 4 dagen stil, dataverlies € 35.000 herstel + omzetderving € 280.000. Post-incident: investering in EDR-systeem, 2FA voor alle externe toegang, maandelijkse phishing-trainingen, offline back-up off-site.

## Bronnen

[^1]: `ISA-315-herzien-2019__sec_bijlage-6-overwegingen-voor-het-verwerven-van-inzicht-in-gen`
