OFFICIAL 

## NatHERS Technical Note 

Nationwide House Energy Rating Scheme[® ] Requirements for NatHERS Thermal and Whole of Home assessments- 

Version: 20241023 

OFFICIAL For use with NatHERS accredited software tools (NatHERS software tools) using CSIRO Chenath engines **3.22 and 3.23** 1 (Note **Version June 2019** for use with software versions using CSIRO Chenath engine 3.21) 

OFFICIAL 



© Commonwealth of Australia 2024 

## **Ownership of intellectual property rights** 

Unless otherwise noted, copyright (and any other intellectual property rights) in this publication is owned by the Commonwealth of Australia (referred to as the Commonwealth). 

## **Creative Commons licence** 

All material in this publication is licensed under a Creative Commons Attribution 4.0 International Licence except content supplied by third parties, logos and the Commonwealth Coat of Arms. 

Inquiries about the licence and any use of this document should be emailed to copyright@dcceew.gov.au. 


## **Cataloguing data** 

This publication (and any material sourced from it) should be attributed as _NatHERS Technical Note Nationwide House Energy Rating Scheme® Requirements for NatHERS Thermal and Whole of Home assessments_ , Version 20241023 Department of Climate Change, Energy, the Environment and Water, Canberra, October 2024. CC BY 4.0. 

This publication is available at www.nathers.gov.au/publications/nathers-technical-note 

Department of Climate Change, Energy, the Environment and Water GPO Box 3090 Canberra ACT 2601 Telephone 1800 920 528 

Web dcceew.gov.au 

## **Disclaimer** 

The Australian Government acting through the Department of Climate Change, Energy, the Environment and Water has exercised due care and skill in preparing and compiling the information and data in this publication. Notwithstanding, the Department of Climate Change, Energy, the Environment and Water, its employees and advisers disclaim all liability, including liability for negligence and for any loss, damage, injury, expense or cost incurred by any person as a result of accessing, using or relying on any of the information or data in this publication to the maximum extent permitted by law. 

## **Acknowledgement of Country** 

We acknowledge the Traditional Owners of Country throughout Australia and recognise their continuing connection to land, waters and culture. We pay our respects to their Elders past and present. 

## **About the Nationwide House Energy Rating Scheme (NatHERS)** 

NatHERS supports improvements to the energy efficiency and comfort of Australia’s dwellings by standardising the approach and guidelines for NatHERS accredited software to assess dwellings across Australia. 

The Australian Government administers NatHERS on behalf of the Commonwealth and state and territory governments. 

**For more information visit** www.nathers.gov.au 

OFFICIAL 


OFFICIAL **Version 20241023 For use with Chenath 3.22 and 3.23** 

## Technical Note change log 

NatHERS software is an energy rating model. All models are representations of realworld scenarios and include approximations and assumptions. NatHERS modelling is based on decades of science and consultation with stakeholders and is under constant review. 

|review.||
|---|---|
|**Version**<br>**number**<br>(YYYYMMDD)|Comments|
|20220608|Draft version for TAC comment|
|20220714|Incorporated TAC feedback. Prototype submitted to Steering Committee|
|20220810|Incorporated TAC feedback. Prototype submitted to ETWG|
|20220817|Incorporated TAC feedback. Prototype submitted to TAC for final review|
|20220901|Final TAC feedback from TAC incorporated. Published version|
|20230913|Incorporated TAC feedback.  Extensive thermal bridging and Whole of Home<br>updates.|
|20230926|Added multi-split air conditioning modelling instructions to 12.3|
|20230929|Editorial updates|
|20231023|Chapter 11 Thermal bridging clarification to Table 8 and footnote|
|20240501|Clarified climate zone selection; default floor coverings; thermal breaks;<br>revised default pool pump star ratings; substitution rules clarified for<br>WERSlink library windows; clarified and revised modelling of heating and<br>cooling appliances 12.2 to 12.6; introduced a new term “bedroom complex”<br>describing a conglomerate of bedroom and its dedicated ensuite and/or WIR<br>and/or hallway – see Hallway definition in Appendix 1.|
|20241023|New clause 12.10 on centralised heat pump hot water proxy for Class 2 buildings.<br>Adjusted default downlight density to 1/5m2, Table 66.<br>Included consideration of NCC class 1b dwellings.<br>Clarified zoning of bathrooms in new Appendix 2|



OFFICIAL 


OFFICIAL 



## Contents 

|---|---|



OFFICIAL 


OFFICIAL 



|---|---|



OFFICIAL 




## OFFICIAL 

## Tables 


OFFICIAL 


OFFICIAL 



## 1. Introduction 

## **Purpose** 

- 1.1 This Technical Note details the requirements that must be followed when conducting a NatHERS assessment in regulation mode for demonstrating compliance to the deemed-to-satisfy NatHERS pathway of the National Construction Code (NCC). It is applicable to both NatHERS accredited assessors and non-accredited assessors. It also forms a part of the End User Licence Agreement which assessors enter into as a condition of using the NatHERS software tools and via their accreditation as a NatHERS accredited assessor. This enables completion of NatHERS assessments in a consistent way. 

- 1.2 Assessors must use this Technical Note for all NatHERS assessments using Chenath engines 3.22 and 3.23. Chenath engines 3.22 and 3.23 are designed for use with NCC 2022. (See also “Regulatory requirements and exemptions” below). 

- 1.3 NatHERS software tools are used to assess new builds and renovations of NCC Class 1a, 1b, 2, and Class 4 parts of buildings. 

   - 1.3.1 For attached Class 10a buildings, these dwellings must also be modelled as part of the assessment. 

   - 1.3.2 For renovations, an assessors must contact their relevant jurisdiction to determine the modelling requirements. 

   - 1.3.3 For class 1b, refer to Table 1. 


|Table 1 - Modelling Class 1b||
|---|---|
|Class 1b scenario|Model|
|≥4 single dwellings on one allotment, each dwelling has a kitchen or<br>kitchenette|Model each dwelling<br>individually as Class 1a|
|≥4 single dwellings on one allotment,**but separate**kitchen/communal<br>area/building|Cannot be modelled in<br>NatHERS|
|Boarding house, guest house or hostel < 300 m2 with multiple<br>bedrooms and shared kitchen, living and bathroom spaces.|Model as single Class 1a<br>dwelling|
|Boarding house, guest house or hostel < 300 m2 with kitchenettes in<br>each bedroom unit and no communal space/s|Model each bedroom unit<br>as individual Class 1a<br>dwellings|
|Boarding house, guest house or hostel < 300 m2 with kitchenettes in<br>each bedroom unit as well as a communal space/s|Model as a single Class 1a<br>dwelling and zone the<br>rooms’ kitchenettes as per<br>Appendix 1, footnote (1)|



OFFICIAL 


OFFICIAL 



- 1.4 NatHERS software tools may be accredited to include a NatHERS Whole of Home assessment which builds on the results of the thermal performance assessment. The additional features include heating and cooling systems, hot water systems, lighting, cooking, plug loads, pools and spas pumps, and onsite energy generation and storage. 

## **Regulatory requirements and exemptions** 

- 1.5 Assessors conducting NatHERS assessments must apply the requirements in this Technical Note unless state or territory regulatory requirements apply. State or territory regulatory requirements, such as the Building Sustainability Index (BASIX) in NSW, prevail in the event of inconsistency. Refer to the NCC for jurisdictional variations or contact the relevant state/territory regulator and/or council for their requirements. Assessors must report any local regulatory requirements they have included in a thermal performance assessment, in the additional notes of the NatHERS Certificate. 

## **Status of this Technical Note** 

- 1.6 This Technical Note prevails in all matters covered by the NatHERS Assessor Handbook, specific software training manuals, help files, technical support, Assessor Accrediting Organisation (AAO) guidance, Registered Training Organisations (RTOs), software trainers and other subject matter experts' advice. 

- 1.7 AAOs may issue additional modelling guidance and practice notes that support this Technical Note. Where there is a perceived contradiction, this Technical Note prevails. 

- 1.8 Where this Technical Note does not cover part of a complex modelling situation, assessors should use their professional judgement. Accredited assessors should contact their AAO support desk for advice to consider before using their own judgement. All supporting information that informs a decision must be kept with the plans and documentation. 

- 1.9 NatHERS software tool providers provide software tool support. The AAOs and the NatHERS Administrator provide modelling support. 

- 1.10 Links to third party websites contained in this document may change outside of the control of the NatHERS Administrator. It is the responsibility of the assessor to locate the updated webpage until such links are fixed in new version of this document. 

OFFICIAL 


OFFICIAL 



## **Quality assurance** 

- 1.11 AAOs regularly conduct quality assurance (QA) and reviews. The client, regulators, AAOs or NatHERS Administrator may request supporting information to conduct QA. The QA will include assessment of adherence to the Technical Note for NCC compliance. As part of QA activities, the NatHERS Administrator and stakeholders may access and use assessment information, and where appropriate, contact affected parties and regulatory authorities. 

## **Consequences of misuse** 

- 1.12 All accredited and non-accredited assessors[1] must follow the requirements of this Technical Note when conducting a NatHERS assessment. This forms a part of the software end user licence agreement for use of NatHERS software tools in regulation mode. Furthermore, all accredited assessors must adhere to the terms of their accreditation as a NatHERS Accredited Assessor. In the case of an inconsistency with the terms of those agreements, this Technical Note prevails except where state and territory requirements overrule it. 

- 1.13 The consequences of not meeting the requirements of the Technical Note may include but are not limited to: 

   - a. suspension or cancellation of accreditation 

   - b. additional quality assurance/reviewing of past and future assessments 

   - c. cancellation of access to NatHERS software tools 

   - d. notification of the relevant regulatory authority by the NatHERS Administrator 


   - f. remedial or disciplinary action in accordance with the AAO protocol 

   - g. voiding the assessors’ professional indemnity insurance and/or 

   - h. future litigation that may be brought upon the assessor. 

## **Updates** 

- 1.14 An update to this Technical Note will be issued from time to time. It is the responsibility of assessors to ensure they are using the appropriate version. The latest version is available from www.nathers.gov.au. Notification of updates will be provided to assessors through their AAOs, software tool providers and jurisdictional building authorities. As corrections and clarifications to this document are developed and before an update to this document is issued, such clarifications may 

> 1 Non-accredited assessors are also referred to as “raters” 

OFFICIAL 


OFFICIAL 


be outlined in the NatHERS Frequently Asked Questions webpage, https://www.nathers.gov.au/resources/faqs. 

- 1.15 The chapter numbering in the NatHERS Assessor Handbook corresponds to the section numbering in this Technical Note. The Handbook provides general principles and assessment guidance to support the Technical Note and is available on the NatHERS website (www.nathers.gov.au). 

- 1.16 Assessors must refer all enquiries and comments about this Technical Note to their AAOs in the first instance, or the state or territory building regulator if assessor accreditation or licensing is not required in the jurisdiction. Where necessary, these organisations will refer the matter to the NatHERS Administrator for advice. The NatHERS Administrator may provide guidance and/or issue an amended Technical Note. 

## **Disclaimer** 

- 1.17 When conducting a NatHERS assessment, the assessor must comply with the material in this Technical Note. It is made available for assessors who use NatHERS software tools in the mode accredited under NatHERS (regulation mode) only and on the understanding that the NatHERS Administrator, the state and territory governments and the Commonwealth (the participating bodies) are not providing professional advice, nor indicating a commitment to a particular course of action. 

- 1.18 Reasonable efforts have been made to ensure the information in this Technical Note is accurate and reliable. The participating bodies and all persons acting for the participating bodies preparing this publication accept no liability for the accuracy of, or inferences from, the material contained in this publication. The NatHERS Administrator expressly disclaims liability for any person’s loss arising directly or indirectly from the use of, inferences drawn from, deductions made from, or actions performed in reliance on this Technical Note. The material in this Technical Note may include the views or recommendations of third parties, which do not necessarily reflect the views of the Participating Bodies or indicate their commitment to a particular course of action. 


## **Correct software version** 

- 2.1 Ensure that you are using the latest version of the NatHERS accredited software (unless alternative state or territory regulatory requirements apply): 

   - a. Class 1 ratings must be started in the latest version of the software. 

OFFICIAL 


OFFICIAL 


   - b. Class 2 ratings, if it is the first dwelling in the development, must be started in the latest version of the software. 

- 2.2 When reviewing and finalising a rating after a building permit has been granted, use the latest version of the NatHERS accredited software (unless alternative state or territory regulatory requirements apply) or, if necessary, use the version that was in place at the time the building permit was granted. You must have a written request from the state or territory building regulator to use the older version. 

## **Conflict of interest declaration** 

- 2.3 Any potential or actual conflict of interest must be outlined in ‘additional notes’ on the NatHERS Certificate, including what the conflict relates to (e.g. financial interest, relationship to certifiers, builders or owners). 

## **Consent to collect and share data** 

- 2.4 Persons performing NatHERS assessments must inform their clients that they will collect personal information, including their name, email address, telephone number, ABN (where applicable), previous NatHERS assessments and design documentation used for the assessments. This information may be disclosed to: 


   - b. the NatHERS Administrator and applicable Assessor Accrediting Organisation (AAO) 

      - for the purposes of quality assurance, investigation and review including consent for these persons/entities to contact the client in relation to any findings relevant to the assessment. 

## **Design documentation** 

- 2.5 The minimum design documentation required when modelling a dwelling is: 

   - a. site plan — including a north point as documented on the survey 


   - c. elevations 

   - d. sections 


   - f. electrical schedule (see Table 6 and Table 10 for default values if this schedule is incomplete) 

OFFICIAL 


OFFICIAL 


- g. window, skylight, roof window and door schedule/details including size, preferred glass and frame type, opening style, location 

- h. appliance, solar panel, battery and pool specifications. 

## 3. Data entry and retention 

- 3.1 NatHERS software tools are used to assess an entire dwelling. Additions or extensions to an existing dwelling must be modelled as part of the entire dwelling. 

- 3.2 Each dwelling must have its own individual rating modelled in accordance with this Technical Note. 

- 3.3 The project details and dwelling modelling must be consistent with the design documentation. 

   - 3.3.1 If the design documentation used for producing a NatHERS Certificate changes and the rating is impacted, the Certificate is no longer valid. A new assessment and NatHERS Certificate must be completed for regulatory approval purposes. 

   - 3.3.2 Where a certificate is generated based on preliminary/draft/not for construction documentation, this must be noted in ‘additional notes’. 

   - 3.3.3 Certificates generated based on design documentation will be preliminary. Final certificate is only issued based on marked For Construction documentation. 

- 3.4 If the assessor recommends a change to any element of the design, the client must update the design documentation before the assessor finalises the assessment and issues the NatHERS Certificate. 

- 3.5 Clarification must be sought from the client where information is ambiguous or inconsistent and any appropriate revisions must be made to the design documentation before issuing a NatHERS Certificate. 

- 3.6 If the client has not provided the required information as specified in 3.5, requests for clarification and client responses must be kept with the assessment for review purposes. 

- 3.7 When modelling Whole of Home, refer to fixed appliance specifications (if available, else select default values). If the specified type of appliance is not available in the software, guidance from the assessor’s AAO or the NatHERS Administrator must be sought and noted in ‘additional notes’ on the NatHERS Certificate. 

OFFICIAL 


OFFICIAL 



## **Defaults** 

- 3.8 An assessment must be undertaken using the default values in this Technical Note where clarification has been sought but not received. The client must be advised that some defaults represent the worst-case scenario and the rating may be adversely affected. 

- 3.9 Any defaults used for the assessment must be detailed in the NatHERS Certificate ‘additional notes’ (excluding default windows, which are itemised separately in the certificate). 

## **Data retention** 

- 3.10 The assessor must retain (for a minimum of seven years or a greater time as required by the jurisdiction) all design, assessment and supporting documentation in line with the jurisdiction’s requirements and for AAO and NatHERS Administrator review and quality assurance purposes. 

## 4. Climate, exposure, ground reflectance and orientation 

## **Climate zone selection** 

- 4.1 In NatHERS software tools, each postcode is allocated a ‘principal climate zone’ and sometimes one or two alternative climate zones. Assessors must use the principal climate zone, unless otherwise permitted by the rules below.  When selecting a climate zone: 

   - 4.1.1 Assessments must use the postcode in NatHERS software tools that corresponds to the location. If a newly developed suburb has not yet been allocated a postcode or the postcode is not available in NatHERS software tools, the postcode of the nearest existing suburb with similar climatic properties must be used. This must be detailed in the ‘additional notes’ section of the NatHERS Certificate. 

   - 4.1.2 If the primary climate zone is not considered representative of the climate on site (e.g. because of a change in altitude), the assessor may choose to use one of the alternative climate zones allocated to the postcode in the NatHERS software tool or available on the NatHERS website. The assessor must not use a climate zone other than those allocated to the postcode. Where the assessor has chosen to use one of the alternative climate zones, 

OFFICIAL 


OFFICIAL 


a justification must be detailed in the ‘additional notes’ section of the NatHERS Certificate. 

## **Exposure categories** 

- 4.2 The exposure category best suited to the terrain surrounding the dwelling must be used. Exposure can vary for different apartments in a single building and this must be considered in assessments. Table 2 provides guidance on the indicative characteristics of exposure categories. 


|Category|Terrain and built environment|Examples|
|---|---|---|
||characteristics||
|Exposed<br>Few or no obstructions<br>or||Flat grazing land, lakeside or ocean frontage,<br>desert, exposed high-rise unit without<br>obstructions at a similar height to the dwelling|
|Open<br>Grasslands with few well scattered<br>obstructions less than or equal to 10 m<br>high||Farmland with scattered sheds, lightly<br>vegetated bush blocks, elevated units with a<br>few obstructions of similar height to the<br>dwelling|
|Suburban<br>Numerous closely spaced obstructions<br>less than or equal to 10 m high||Suburban housing, heavily vegetated bushland<br>areas, townhouses|
|Protected<br>Numerous closely spaced obstructions<br>greater than 10 m high||City and industrial areas|



OFFICIAL 


OFFICIAL 





Category  Terrain and built environment  Examples<br>characteristics<br>


## **Ground reflectance** 

- 4.3 A ground reflectance setting of 0.2 must be modelled at all times. 

## **Orientation** 

- 4.4 Dwelling orientation must be based on the rotation of the dwelling with respect to true north, not magnetic north. 

- 4.5 If assessors are unsure whether the plans are depicting true or magnetic north, they must clarify the direction of true north. 

## 5. Zoning 

## **Zone types** 

- 5.1 Assessors must assign zones for all parts of the dwelling that can be fully enclosed by the dwelling envelope (the physical separator between the dwelling being assessed and the outside environment or neighbour). **Appendix 1** outlines software zoning type definitions and requirements. 

   - 5.1.1 All parts within the dwelling envelope must be allocated or included in a zone. 

   - 5.1.2 **Conditioned** outdoor living areas (i.e. mechanically heated or cooled) must be considered within the dwelling envelope and assigned a zone when capable of being fully enclosed by solid construction elements (e.g. walls, windows, bi-fold or sliding doors). 

   - 5.1.3 **Unconditioned** outdoor living areas (enclosed or partially open), ‘alfresco’ spaces and detached garages are not allocated a zone and are an 

OFFICIAL 


OFFICIAL **Version 20241023 For use with Chenath 3.22 and 3.23** 

exception. These areas must be considered for shading purposes only (See Appendix 1 for further details). 

## **Minimum zoning requirements** 

- 5.2 All dwellings must: 

   - a. contain one main kitchen/living zone 

   - b. contain a minimum of three zones excluding the garage (e.g. a kitchen/living, bedroom and an unconditioned zone) 

   - c. have walls, a floor and a ceiling and/or a roof for each zone. 

- 5.3 

- Studios, bedsits and open-plan apartments must: 

- a. contain at least three zones (kitchen/living, bedroom and an unconditioned zone) and 

- b. when there are no obvious features by which to zone the open-plan studio or bedsit, then (for modelling purposes only): 

   - i. kitchen/living zone floor area(s) = minimum of 30% 

   - ii. bedroom zone floor area = minimum of 20% and 

   - iii. these two zones shall be separated by an artificial plasterboard-on-stud internal dividing wall(s) with a wall area of no less than 40% between zones. 

## **Combining zones** 

- 5.4 There are only two situations where zones may be combined: 

      - i. Spaces within a garage such as workshops, storerooms, spaces under stairwells, WCs and laundries may be combined with that are within the garage 

   - b. If the dwelling contains more than 50 zones, adjacent zones (e.g. bedrooms) may be combined if they meet all of the following: 

      - i. have external windows or doors to the same orientation (i.e. do not have external ventilation to more than one orientation) 

      - ii. are the same zone and conditioning type and 

      - iii. open to the same internal zone (e.g. an internal hallway). 

## **Bathrooms, WCs and ensuites** 

- 5.5 Appendix 2 provides a flowchart to correctly zone bathrooms, WCs and ensuites. 

OFFICIAL 


OFFICIAL 


- 5.6 All dwellings must have at least one bathroom/WC that is available for general use (these may be combined or in separate rooms). They must be zoned as: 

   - a. parent zone if they have no external openable windows or doors or 

   - b. unconditioned if they have external windows or doors and can be closed from the main dwelling or 

   - c. according to the parent zone if they cannot be closed from the main dwelling and there is a permanent opening to the parent zone. 

- 5.7 For NatHERS purposes, an ensuite is considered a bathroom associated with a bedroom. If it is also intended for general household use, it is modelled as a general use bathroom. 

## **Unconditioned zones** 

- 5.8 Every dwelling must have at least one unconditioned zone. 

- 5.9 Laundries must be zoned unconditioned if they have external windows or doors and can be closed from the main dwelling (otherwise see clause 5.5) 

- 5.10 An airlock is a small, relatively airtight space that can be modelled as unconditioned space if it: 

   - a. is located at a dwelling entrance 

   - b. has one or more external wall 

   - c. has one or more internal wall 

   - d. has an external door and 

   - e. has one or more internal doors, of which only one opens to a conditioned zone. 

   - 5.10.2 Where an area labelled as an airlock does not meet the conditions of clause 5.10, it must be modelled as a daytime zone. 

- 5.11 If no rooms fit the definition of unconditioned, then choose the smallest zone and model this as unconditioned. 

## 6. Floors 

Thermal bridging – see section 11 

## **Waffle pods** 

- 6.1 Where expanded polystyrene (EPS) waffle pods are specified, assessors must use the waffle pod thickness: 

OFFICIAL 


OFFICIAL 


   - a. closest to the dimension indicated on the design documentation, but never higher, and 

   - b. measured from the underside of the top slab to the bottom of the waffle pod construction. 

- 6.2 Where the waffle pod thickness is not shown on the design documentation, the default 175mm thickness option must be used. 

- 6.3 Unless otherwise shown on the plans a default 85 mm concrete cover must be applied to the waffle pod. 

## **Non-insulating void-forming constructions** 

- 6.4 For the purpose of a NatHERS assessment, any non-insulating void-forming construction must currently be modelled as a conventional concrete slab-on-ground construction where: 

   - a. thickness = the thickness of the top continuous concrete layer 

   - b. floor height above ground = the total depth of the void former plus the continuous concrete cover 

      - and 

   - c. if there is a reflective membrane underneath, include a horizontal air gap >66 mm (90 nominal), unventilated, reflective (0.2/0.9; E = 0.20). 

## **Floor coverings and underlays** 

- 6.5 Where no floor coverings are specified, assessors must use the following defaults: 

   - a. garages have concrete floors 

   - b. wet areas, butler’s pantries and kitchens have ceramic tiles 

   - c. small storage and void spaces have the same floor finish as the parent zone 

   - d. where a software tool models an **artificial** floor in a double height void zone, there is no floor covering 

   - e. all other areas have carpets with rubber underlay. 

- 6.6 If the floor covering material colour is not specified on the drawings the default colour of medium (solar absorptance = 0.5) must be modelled. 

## **Dwellings above car parks and public spaces** 

- 6.7 Assessors must model dwellings directly adjacent to carparks and public spaces as per Table 3. 

OFFICIAL 


OFFICIAL 




|||Construction feature of the dwelling being rated|Construction feature of the dwelling being rated|Construction feature of the dwelling being rated|Construction feature of the dwelling being rated|
|---|---|---|---|---|---|
||Adjacent area|Adjacent to floor|Adjacent to ceiling|Adjacent to wall|**Dwelling**<br>**entrance**<br>**door**|
|1.|Apartment|Neighbour|Neighbour|Neighbour|Model 0%<br>openability|
|2.|Shared basement carpark —<br>enclosed|Shared basement<br>carpark zone2|--|Shared basement<br>carpark zone|Model 0%<br>openability|
|3.|Shared basement or above-<br>ground carpark — ventilated|Outside air|Outside air|Outside air|Model 0%<br>openability|
|4.|Garage (private) —<br>accessed from dwelling and<br>own vehicular access door<br>**NOT**part of larger enclosed<br>basement carpark|Garage zone|Garage zone|Garage zone|Model 0%<br>openability|
|5.|Garage (private, walled) —<br>accessed from dwelling and<br>own vehicular access door and<br>**PART OF**larger enclosed<br>basement carpark|Shared basement<br>enclosed carpark<br>zone|Shared basement<br>enclosed carpark<br>zone|Shared basement<br>enclosed carpark<br>zone|Model 0%<br>openability|
|6.|Commercial premises|Neighbour|Neighbour|Neighbour|Model 0%<br>openability|
|7.|Common corridor —<br>no glazing, conditioned,<br>enclosed|Neighbour|Neighbour|Neighbour|Model 0%<br>openability|
|8.|Common corridor —<br>no glazing, unconditioned,<br>enclosed3|Neighbour|Neighbour|Neighbour|Model 0%<br>openability|
|9.|Common corridor — with<br>glazing, unconditioned,<br>enclosed|Glazed common<br>area zone4|Glazed common<br>area zone|Glazed common<br>area zone|Model 0%<br>openability|
|10.|Common corridor —<br>withglazing,conditioned|Neighbour|Neighbour|Neighbour|Model 0%<br>openability|
|11.|Common corridor —<br>with permanent opening to<br>outside air|Outside air|Outside air|Wall with eaves<br>same length &<br>width|Model<br>documented<br>openability|



2  An enclosed carpark has an external wall either fully adjacent to earth or less than 50% of the wall height is exposed to air. Model entire zone including floor (only the level directly adjacent to the dwelling and assume it is on ground); external walls and their adjacencies (including the underground external walls as retaining walls with a 5m thick soil layer), ceilings and roofs and their adjacencies. 

3  e.g. corridors accessible via lifts, or stairwells, or with an airlock between corridor and external air 4  This applies if: 

- the apartment wall is adjacent to any glazing or 

- the apartment is directly opposite any glazing and closer than 3 times the height of the corridor’s ceiling (e.g. if the ceiling is 3 metres high, model apartments opposite any glazing if they are within 9 metres) 

For the glazed common corridor, model either: 

- entire zone or 

- zone section adjacent to the apartment wall and including the relevant glazed element. If needed, the zone can be enclosed by an artificial internal wall with adjacency to neighbour. 

OFFICIAL 


OFFICIAL 



|12.|Common public area — mostly<br>enclosed|Neighbour|Neighbour|Neighbour|Model 0%<br>openability|
|---|---|---|---|---|---|
|13.|Common public area — highly<br>ventilated|Outside air|Outside air|Outside air|Model<br>documented<br>openability|
|14.|Lift|Neighbour|Neighbour|Neighbour|Model 0%<br>openability|
|15.|Stairwell — enclosed|Neighbour|Neighbour|Neighbour|Model 0%<br>openability|
|16.|Stairwell – open|Outside air|Outside air|Outside air|Model<br>documented<br>openability|



## 7. Walls 

Thermal bridging – see section 11. 

## **Exterior colour** 

- 7.1 Assessors must model the exterior wall colour or solar absorptance as detailed on the design documentation. In the absence of a solar absorptance value, this may be calculated as follows: 


- 7.2 Where no exterior wall colours, solar reflectance or absorptance are specified, assessors must select the default colour as medium. 

## **Internal colour** 

- 7.3 Where there is an option to nominate an internal wall colour in the software and no internal wall colours are specified on the design documentation, assessors must select the default internal wall colour as medium. 

## **Insulation** 

- 7.4 Where insulation is added to a wall, assessors must remove **any** air gap thickness that has been filled by bulk insulation. 

## **Earth materials** 

- 7.5 [Under preparation, to be included in future Tech Note.] 

OFFICIAL 


OFFICIAL **Version 20241023 For use with Chenath 3.22 and 3.23** 


- 8.1 All garage doors and windows must be modelled as shown in Table 4 unless specified otherwise in the design documentation. 


||Unconditioned garage|Conditioned garage|
|---|---|---|
|External doors|Not weather-stripped|Weather-stripped|
|Windows|Not weather-stripped<br>With insect screen|Weather-stripped<br>With insect screen|



## **Glazed doors** 

- 8.2 Fully or partially glazed hinged doors and sliding doors are considered to be windows in NatHERS software tools. Only the glazed portion of a partially glazed door is to be modelled as a window. The remaining component of the partially glazed door is to be modelled as a solid door. 

   - 8.2.1 If the glazing component is less than 25% of the door, the door may be modelled as a solid door. 

## **Default and custom windows** 

- 8.3 NatHERS will soon have two default window libraries: the current NatHERS default window library and the new WERSLink[5] default window library. Both will be available in software using Chenath 3.23. 

When modelling windows or glazed doors, assessors must use either: 

   - a. the Australian Fenestration Rating Council (AFRC) custom window codes corresponding to the windows specified on the design documentation, found in the NatHERS and WERSlink custom window libraries, or 

   - b. the WERSlink default window library (when available in the software), or 

   - c. the NatHERS default window library. 

- 8.4 If the software is using the WERSlink custom window library and a window is specified on the design documentation that is not available, an assessor must choose a default window from: 

> 5 The Australian Glazing and Window Association’s (AGWA’s) Window Energy Rating Scheme (WERS) Link portal is now complete. The WERSLink will underpin new custom and default window libraries, improving the way assessors can model windows. The new libraries will be incorporated into software using Chenath 3.23. 

OFFICIAL 


OFFICIAL 



      - a. the WERSlink default window library with the specified opening type, or 

      - b. the NatHERS default window library with the specified opening type. 

- 8.5 If the software is using the NatHERS custom window library and a window is specified on the design documentation that is not available, assessors must choose either: 

   - a. a default window from the NatHERS default window library with the specified opening type or 

   - b. an available custom window from the NatHERS custom window library that meets the following three conditions, any substitutions must be itemised in ‘additional notes’: 

      - i. identical opening type (e.g. fixed, awning, casement, sliding) to the window specified on the documentation 

      - ii. a total window system U-value (Uw) equal to, or greater than, the window specified on the documentation (e.g. if the Uw of the specified custom window is 1.5, the modelled window selected could be 2.0) and 

      - iii. a total window system Solar Heat Gain Coefficient (SHGCw) of ±5% of the window specified on the documentation. 

Substituted values must be based on the Australian Fenestration Rating Council 

(AFRC) protocol rather than, for instance, the European ratings. 

- 8.6 When using default windows, obscure glass (for instance, in a bathroom or WC) may be considered as either: 

   - a. clear if the glass is clear patterned, or 

   - b. tinted if the glass has a tint or translucent laminate. 

- 8.7 In the absence of obscure glass in the custom windows library, assessors must model either: 

   - a. a default clear window if the glass is clear patterned, or 

   - b. a default tint window if the glass is a tint or translucent laminate, or 

   - c. if the glass is clear patterned then a clear window from the same range of custom windows that is being used (i.e. same frame type and frame material), or 

   - d. if the glass is tinted or translucent laminate, then a tinted window from the same range of custom windows that is being used (i.e. same frame type and frame material) must be modelled. 

- 8.8 When using the NatHERS default window library and openability is unknown, apply the default opening percentage in 

- 8.9 Table 5. This reflects the area of window that can open and deducts a percentage for the window frame. 

OFFICIAL 


OFFICIAL 


- 8.10 Where there is an option to nominate a window frame colour in the software and no window frame colours are specified on the design documentation or available on request, assessors must select the default window frame colour as medium (solar absorptance = 0.5). 

- 8.11 Combinations of NatHERS default windows that comprise various glazing components and opening styles, and therefore fall outside the parameters of 

- 8.12 Table 5, must be entered into the NatHERS software as 


Where: 

a = the sum of each glazing component’s area multiplied by its corresponding default opening percentage[7] (i.e. the sum of each component’s openable area) based on 

Table 5 

b = the total area of the whole (combination) window 

c = the percentage openability of the whole (combination) window 

Note: 

   - i. This formula can be applied to any configuration of combination window with both fixed and openable component/s to calculate its total opening percentage. 

   - ii. Use the window code that corresponds to the glazing component with the largest window openability. 

- 8.13 To meet restricted opening safety requirements, where a complying security screen is absent, assessors must adjust window opening percentages. If the restricted opening percentage is not specified on the design documentation or product manufacturer’s specifications, where they are required[8] assessors must use the default opening percentage of 10% for all openable window types 

> 6 Refer to Assessor Handbook section 8.4 

> 7 If security restrictors apply, a default opening percentage of 10% must be applied for each window unit this is relevant to, unless otherwise specified. 

> 8 Refer to the relevant jurisdiction’s requirements 

OFFICIAL 


OFFICIAL 




|5 – NatHERS default window opening percentages||
|---|---|
|Type|**Default**<br>**opening**<br>**percentage**|
|Fixed|0%|
|Operable component||
|WITH restricted opening safety requirements||
|All windows types shown with safety restrictors (see 8.13)|10%|
|WITHOUT restricted opening safety requirements8||
|Double hung|45%9|
|Sliding|45%10|
|Awning|90%|
|Casement / tilt and turn|90%|
|Louvre|90%|




For thermal bridging – see section 11 

## **Roof colour** 

- 9.1 Assessors must model the roof colour and solar absorptance as detailed on the design documentation. If only a roofing material manufacturer’s colour is specified then the solar absorptance can be taken from the manufacturer’s colour charts. Alternatively, in the absence of a solar absorptance value, this may be calculated as follows: 


- 9.2 Where the roof colour or solar absorptance is not detailed on the design documentation, the assessor must select the default roof colour as medium (solar absorptance = 0.5). 

## **Ceiling colour** 

- 9.3 Where there is an option to nominate a ceiling colour in the software and no ceiling colour is specified in the design documentation, assessors must select the default internal ceiling colour as medium. 

> 9 Two window sashes where the movable sash, or sashes, can open a maximum of 45% of the entire window 

> 10 Sliding window or door where the movable sash opens a maximum of 45% of the entire opening 

OFFICIAL 


OFFICIAL 



## **Ceiling penetrations** 

- 9.4 Assessors must model all recessed light fittings (referred to as downlights), vents, flues, chimneys, fireplaces and exhaust fans as ceiling penetrations. 

- 9.5 Assessors must input information about ceiling penetrations in accordance with the dwelling’s documentation. 

- 9.6 If any of the ceiling penetration information for the dwelling is unspecified or incomplete, apply the defaults in Table 6. Existing parts of dwellings undergoing a major renovation will require informed assessor discretion as the Table 6 defaults may be inappropriate. 


|Type|How to model defaults|
|---|---|
|No lighting specifications|•<br>Sealed<br>•<br>1 downlight per 5m2or part thereof<br>•<br>90 mm diameter<br>•<br>50 mm insulation clearance|
|Lights indicated, but no details|•<br>Sealed downlight<br>•<br>50 mm insulation clearance|
|Exhaust fan unducted|•<br>sealed in conditioned zones<br>•<br>unsealed in unconditioned zones<br>•<br>250 mm diameter<br>•<br>50 mm insulation clearance|
|Exhaust fan ducted|•<br>sealed in conditioned zones<br>•<br>unsealed in unconditioned zones<br>•<br>250 mm diameter<br>•|
|Kitchen rangehood|•<br>250 mm diameter sealed exhaust fan<br>•<br>50 mm insulation clearance|
|Fan light heater|•<br>sealed in conditioned zones<br>•<br>unsealed in unconditioned zones<br>•<br>250 mm exhaust fan<br>•<br>50 mm insulation clearance|
|Heating device flue|•<br>Add 100 mm clearance if flue diameter is known<br>•<br>If flue diameter is not known allow a total of 300 mm<br>insulation clearance|



- 9.7 Downlights must be modelled regardless of the adjoining zone (e.g. roof space, neighbour or second storey floor). 

- 9.8 Treat permanent static ventilation openings in the building fabric (e.g. unflued gas heater vent) as a wall or ceiling vent. 

OFFICIAL 


OFFICIAL 



## **Insulation** 

- 9.9 Assessors must model any edge batts shown in the documentation. If insulation value is not specified, the default R3.0 and 450 mm width must be applied. 

## 10. Shading 

- 10.1 Assessors must model all fixed and non-fixed shade features shown in the documentation. 

- 10.2 Where there is a limit to the number of shading features that can be modelled in the NatHERS software tool, model the three that have the largest impact on the NatHERS thermal performance rating. 

## **Eaves and horizontal shading device** 

- 10.3 Assessors must model the width of an eave or horizontal shading device from the face of the external wall to the bottom of the fascia board or the underside of the outer edge of the horizontal shading device. Gutters may be modelled at the assessor’s discretion. 

## **Vertical shading features including neighbouring buildings** 

- 10.4 Assessors must model neighbouring buildings and surrounding topographical features that obstruct the sun. Assessors must model all single-storey neighbours within 10m and two-storey or higher neighbours within 20m of the dwelling. Assessors must consider the impact of level changes and retaining walls when modelling these features. 

- 10.5 

   - Shade feature modelling: 

   - a. south of the Tropic of Capricorn – ignore features within SSE and SSW, (168⁰45’ and 191⁰15’), 

   - b. north of the Tropic of Capricorn – model all features. 

- 10.6 Where information on neighbouring buildings and fences is not shown on the design documentation, assessors must request the documentation be updated or obtain supporting evidence of existing neighbouring buildings for the purpose of modelling (e.g. Google maps). 

- 10.7 Where neighbouring buildings are unknown because the dwelling is located in a new development, the following defaults must be applied: 

OFFICIAL 


OFFICIAL 



   - 10.7.1 The neighbouring building’s footprint will match the design being modelled, having the same floor, wall and roof height (e.g. a two-storey dwelling should presume a two-storey neighbour), length, width and orientation as the one being modelled. 

   - 10.7.2 The setback from the street of the neighbouring building is to be the same setback from the street as the dwelling being rated. 

   - 10.7.3 The side and rear fence heights of the neighbouring building are to be 1.8m if local planning requirements are unknown. 

   - 10.7.4 Heights of the neighbouring building are to be modelled to include all known site level changes that will impact on shading of the dwelling being rated. 

   - 10.7.5 A neighbouring building’s setbacks must be located parallel to the fence line and at a distance equal to the shortest distance between the rated building and the fence line. This setback is to be calculated independently for each boundary where a neighbour is required to be modelled. Ignore neighbouring unattached dwellings to the south except if the dwelling is north of the Tropic of Capricorn (refer 10.5). 

- 10.8 For any fixed vertical screens apply the shading factor of the screen material according to the design specifications. Privacy screens must not be modelled with a 100% shading factor i.e. be completely opaque. If an adjustable screen is being modelled, summer and winter shading factors should be applied according to the design specifications. 

## **Glazed verandahs, loggias, winter gardens or porticos** 

- 10.9 Assessors must treat spaces which are not “zones”, e.g. balconies or other similar spaces with solid, glazed or partially glazed walls attached to either side of the parent wall, as wing walls. 

- 10.10 Assessors must treat balcony walls with solid building elements directly in front of the parent wall as a vertical shading device (i.e. external screen), and model: 

   - a. 100% shading for the portion of the wall that is solid 

   - b. 10% shading for the portion of the wall that is glazed. 

## **Protected trees** 

- 10.11 Only trees with an existing preservation order or heritage protection must be modelled. No other vegetation may be modelled as shade. The design documentation must include: 

   - a. the tree canopy drawn to scale or dimensioned and 

OFFICIAL 


OFFICIAL 


b. existing preservation order or heritage listing. 10.12 May include a species shading schedule. 

## 11. Thermal bridging 

## **Applicable building elements** 

11.1 Thermal bridging only applies to repeating steel frame elements: 

- a. where insulation is interrupted by steel framing elements and 

- b. that are a floor, wall, ceiling, or roof as per Table 7. 


|Building element|When to apply thermal bridging11|
|---|---|
|External walls (Class 1)|Apply<br>Ignore external walls of attached**un**conditioned garage.|
|Apartment external<br>walls (Classes 2 and 4)|Apply if adjacent to non-neighbour public areas such as open12stair<br>wells, open corridors, car parks, garages and other shared public<br>spaces.<br>Ignore if adjacent to neighbour.|
|Internal walls (Class 1<br>and 2)|Apply if adjacent to:<br>•<br>unconditioned garages<br>•<br>roof space or<br>•<br>subfloor zones.<br>Ignore all other internal walls.|
|Ceilings|Apply to ceilings:<br>•<br>below a roof space<br>•<br>in non-neighbour public areas or<br>•<br>directly attached to roof (e.g. flat, skillion or cathedral roof).<br>Ignore if adjacent to another zone (excluding roof space).|
|Floors|Apply to suspended floors above:<br>•<br>outside air (including sub-floors)<br>•<br>unconditioned garage<br>•<br>“non-neighbour” public areas (see Table 3).<br>Ignore if:<br>•<br>in-between floors of multi-level dwellings<br>adjacent to neighbour.|



11 Assessors may also model the effects of thermal bridging for additional features if they exist, to improve the thermal modelling accuracy and if the software allows using appropriate thermal modelling techniques. 12 Open = permanent opening to the outside 

OFFICIAL 


OFFICIAL 


## **Steel frame dimensions** 

- 11.2 If the software has the functionality to enter metal framing specifications, this may be used to apply thermal bridging to the relevant elements. 

- 11.3 Where no framing details are specified in the design documentation, assessors must select the defaults provided in Table 8 if available in the software. 


|Building feature|Frame element|**Steel frame**<br>**dimensions**|
|---|---|---|
|Ceiling/roof without roof cavity<br>(flat, skillion or cathedral roof)|Rafter|200 x 75 mm|
||Rafter spacing|900 mm|
||Flange width|75mm|
||Base metal thickness|1.5 mm|
|Ceiling with roof cavity – trussed<br>or raftered roofs horizontal<br>ceilings.|Truss chord/ceiling joist|90 x 40 mm|
||Joist spacing|900 mm|
||Flange width|40 mm|
||Base metal thickness|0.75 mm|
|Wall|Stud|90 x 40 mm|
||Stud spacing|600 mm|
||Flange width|40 mm|
||Base metal thickness|0.75 mm|
||Nogging dimensions|90 x 40 mm|
||Nogging spacing|1200 mm|
|Floor|Joist|100 x 50 mm|
||Joist spacing|450 mm|
||Flange width|50 mm|
||Base metal thickness|1.5 mm|



## **Thermal breaks** 

- 11.4 Thermal breaks can be modelled only after thermal bridging is applied. They include materials[14] with an R-value greater than or equal to R0.2 and must separate the metal frame from the cladding. 

- 11.5 The assessor must model any thermal breaks specified in the design documentation in accordance with the software’s instructions. 

> 13 Refer to the Assessor Handbook section 11.2 Modelling thermal bridging 

14 E.g. timber battens great than or equal to 20 mm thick, expanded polystyrene strips greater than or equal to 12mm thick or continuous thermal breaks such as polystyrene insulation sheeting. 

OFFICIAL 


OFFICIAL 



- 11.6 When thermal breaks are not specified in the design documentation, assessors must select the defaults provided in Table 9. 

## **NatHERS treatment of airspaces adjacent to framing** 

- 11.7 To align NatHERS modelling with established thermal bridging calculation methods, assessors must enter an additional R0.16 air gap to the construction scenarios shown in Table 9. Refer to individual software guidance notes for specific modelling instructions. 


|Element|Construction|**Thermal**<br>**Break**<br>**minimum**<br>**R0.215 16**|**Air gap**<br>**R0.1617**|
|---|---|---|---|
|External walls|Cavity18|No|Yes|
||Lightweight cladding19(direct fixed to the same insulated<br>steel member as the wall lining, or does not have a wall<br>lining)|Yes|No|
||Lightweight cladding (battened-out by secondary metal<br>members fixed to the frame)|No|Yes|
|Internal walls<br>to<br>unconditione<br>d space/s|Cavity|No|Yes|
||Lightweight cladding (direct fixed to the same insulated<br>steel member as the wall lining, or does not have a wall<br>lining)|Yes|No|
||Lightweight cladding (battened-out by secondary metal<br>members fixed to the frame)|No|Yes|
|Roofs|Roof above attic space|No|No|
||Skillion or cathedral metal roof (metal sheet roofing and<br>ceiling lining direct fixed to main frame)|Yes|No|
||Skillion or cathedral metal roof battened-out by secondary<br>metal members, with or without a ceiling lining|Yes|Yes, if<br>ceiling<br>battens are<br>present<br>1 x R0.16|
|Ceilings|Ceilings below attic spaces|No|Yes|



> 15 Thermal breaks are materials with an R-value greater than or equal to R0.2 installed at all points of contact between the external cladding and the frame. This includes, but is not limited to, materials such as timber battens greater than or equal to 20 mm thick, expanded polystyrene strips greater than or equal to 12mm thick or continuous thermal breaks such as polystyrene insulation sheeting. 

16 NCC 2022 compliant construction includes a minimum thermal break R0.2. 

17 If the software has the functionality 

- 18 e.g. masonry or brick veneer 

19 Lightweight cladding includes weatherboard, fibre-cement, or metal clad. 

OFFICIAL 


OFFICIAL 



||Floors|Suspended floor above enclosed subfloor space|No|Yes|
|---|---|---|---|---|
|||Suspended floor above unconditioned garage, outdoor air<br>or non-neighbour|No|No|



## **Additional modelling guidance** 

- 11.8 If continuous insulation is applied directly adjacent to and touching the steel frame, this should currently be modelled by: 

   - a. Modelling the insulation according to the software’s instructions, e.g. as a separate construction layer, and 

   - b. ticking the thermal break box R0.2. 

- 11.9 Roof blankets - roof blankets do not currently need to be modelled for thermal bridging. 

OFFICIAL 


OFFICIAL 



## 12. Appliances (Whole of Home assessments only) 

## **Defaults for appliances and systems** 

12.1 Where appliance or system are unknown, use the default values in Table 10 and they must be noted in the ‘additional notes’ field of the NatHERS Certificate. 


|Appliance or system|Technology|**Performance level**<br>**/ rating**|
|---|---|---|
|Heating in colda climate|Room reverse cycle air conditioner|HSPF: 2.5<br>Star rating: 1.0|
|Heating in mixed/averageb<br>climate|Room reverse cycle air conditioner|HSPF: 3.5<br>Star rating: 2.0|
|Heating in hotc and humid<br>climate|Room reverse cycle air conditioner|HSPF: 4.0<br>Star rating: 2.5|
|Cooling in colda climate|Room reverse cycle air conditioner|TCSPF: 3.5<br>Star rating: 2.0|
|Cooling in mixed/averageb<br>climate|Room reverse cycle air conditioner|TCSPF: 3.5<br>Star rating: 2.0|
|Cooling in hotcand humid<br>climate|Room reverse cycle air conditioner|TCSPF: 4.0<br>Star rating: 2.5|
|Wood heater|Slow combustion|60%|
|Hot water|**Choose one of two options:**<br>Gas storage system where reticulated gas is<br>available at the dwelling (i.e. at least 1 gas<br>appliance has been specified in the dwelling)|Star rating: 4.0|
||**OR**<br>Electric storage hot water system – off peak, where<br>reticulated gas is not available at the dwelling (i.e.<br>no gas appliances have been specified for the<br>dwelling).|Performance not<br>entered by assessor|
|Lighting|5 W/m2||
|Cooktops|**Choose one of two options:**<br>Gas where reticulated gas is available at the<br>dwelling (i.e. at least 1 gas appliance has been<br>specified in the dwelling)|Performance not<br>entered by assessor|
||**OR**<br>Electric where reticulated gas is not available at<br>the dwelling (i.e. no other gas appliances have<br>been specified for the dwelling).|Performance not<br>entered by assessor|
|Ovens|Electric|Performance not<br>entered byassessor|
|Pools and spas|Pools or spas cannot be included in rating if not<br>specified in design documentation|n.a.|



OFFICIAL 


OFFICIAL 



|Poolpumptype20|Single speed|1 star|
|---|---|---|
|Pool pump star ratings|Single speed:<br>Dual speed:<br>Multi-speed/variable:|1 star<br>3 stars<br>5 stars|
|Solar PV|System cannot be included in rating if not specified<br>in design documentation|n.a.|
|Solar PV inclination (slope)||Same as<br>documented roof<br>pitch where array<br>will be installed|
|Solar PV direction (azimuth)||Same as<br>documented roof<br>direction where the<br>array will be<br>installed|
|Solar PV inverter capacity||Total system size<br>(kW)x 0.75|



- a Cold climates zones: 14, 18, 20, 21, 22, 23, 24, 25, 26, 47, 48, 49, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69 

- b Mixed/average climate zones: 6, 8, 9, 11, 12, 13, 15, 16, 17, 19, 27, 28, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 56 

- c Hot / humid climate zones: 1, 2, 3, 4, 5, 7, 10, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 

## **Heating and cooling** 

- 12.2 Assessors must model the heating and cooling appliance type for each NatHERS conditioned zone as shown on the design documentation. If no appliance is specified the assessor must apply either: 

   - a. the same appliance as is applied to the parent zone; or 

   - b. the default heating and cooling appliances shown in Table 10. 

   - 12.2.2 Where more than one heating or cooling appliance is present in a zone, the assessor must model the heating or cooling appliance with the highest energy consumption. This may require multiple simulations to determine. A wood heater should not be considered in this calculation unless it is the only heater in the zone. 

- 12.3 In the case of a ducted system, the assessor must model a **ducted** system and define all zones it services. 

- 12.4 In the case of a multi split system, the assessor must model a **non-** ducted system and define all zones it services. 

- 12.5 In situations where a heating and/or cooling appliance is not required to carry an energy rating (e.g. multi-split, ducted systems etc), no star rating is displayed. These systems are still required to be tested by GEMS to establish the annual energy 

> 20 Can only be applied if the pool/spa volume is known 

OFFICIAL 


OFFICIAL 


efficiency ratio (AEER) and/or annual coefficient of performance (ACOP) of the outdoor compressor. 

- 12.5.1 If the software has the functionality that allows you to enter the AEER and ACOP, you can find the AEER and ACOP on the Greenhouse & Energy Minimum Standards Regulator energy rating website.  You will need to look for your system outdoor compressor in the *.csv file. The ACOP and AEER values are the last two columns of this file. 

- 12.5.2 The use of manufacturer specified ACOP or AEER is not acceptable. 

## **Hot water systems** 

- 12.6 Assessors must enter the hot water system specified by the design documentation. 

- 12.7 If no hot water system is specified, the assessor must select one of the defaults shown in Table 10. 

- 12.8 

- Solar photovoltaic diverter (PV diverter) hot water system 

- 12.8.1 If a PV diverter hot water system is specified and the software has the capability to model this system, the assessor must select one of 3 types (Table 11) and provide the required evidence of the system being used. 

- 12.8.2 If the software cannot model PV diverters, then that software cannot be used to model a Whole of Home rating for a dwelling that has a PV diverter specified. 


|PV diverter type|Details|Documentary evidence|
|---|---|---|
|Type 1:<br>Simple timer|A standard electric storage hot water<br>system with a timer installed so it heats<br>water during the day rather than<br>overnight|Energisation profile for the<br>system|
|Type 2:<br>Modulated input into an<br>existing storage tank –<br>add-on product|A system with a retrofitted external<br>control added to an existing standard<br>electric storage hot water system. The<br>controller monitors the house load and<br>PV generation and diverts any excess<br>local PV generation to the water heater.|Manufacturer’s product<br>sheet of add-on product|
|Type 3:<br>Bespoke PV Diverter -<br>dedicated product|A specifically designed system where<br>the controller monitors the house load<br>and local PV generation and diverts<br>excess solar energy to the water heater.|Manufacturer’s product<br>sheet of system|



- 12.9 Small Technology Certificates (STCs) for heat pumps and solar hot water 

   - a. STCs are used in NatHERS Whole of Home as a proxy for energy efficiency. The Clean Energy Regulator maintains a register of solar and heat pump water heaters that are eligible for STCs at 

OFFICIAL 


OFFICIAL 



https://www.cleanenergyregulator.gov.au/RET/Scheme-participants-andindustry/Agents-and-installers/Small-scale-systems-eligible-forcertificates/Register-of-solar-water-heaters 

- b. For solar models, follow solar water heater models with a capacity of less than 700 L for heat pump models follow air source heat pumps with a capacity of no more than 425 L. 

- c. In the relevant register, find the model to be installed and enter the required STC for the relevant zone from the table for this model. Note there are four zones in Australia for solar and five zones for heat pump models. 

- d. If the project is in a CER zone other than 3, and the tool require a zone 3 STC for the product, enter the STC in zone 3 for the system as well. This is a software requirement used to populate the certificate hot water schedule substitution range. 

- e. Assessors should **not** apply the number of STCs from the Clean Energy Regulator online calculator. The number of STCs in the calculator is not the 10-year STC for the model. 

## **Centralised heat pump hot water in Class 2 buildings** 

- 12.10 Where apartment buildings of four storeys or more are serviced by a centralised heat pump hot water system, a proxy can be modelled. Refer to proposed modelling flowchart in Figure 1. 

OFFICIAL 


OFFICIAL 



## **Figure 1 - Centralised heat pump hot water proxy** 



Project is in CER heat<br>pump zones 3, 4 or 5<br>yes<br>Class 2 ≥ 4 storeys with<br>centralised heat pump hot<br>water (NOT gas or electric<br>instant  or storage)<br>yes<br>NCC/BCA pipe<br>insulation requirements<br>met<br>yes<br>Continuous tariff<br>yes<br>Closed loop piping<br>(circulatory i.e. not<br>reticulated)<br>no yes<br>Cannot be  Enter STC:<br>modelled in  25 STC for CER zone 3 or<br>NatHERS 27 STC for CER zones 4 and 5<br>


- 12.11 The assessor shall model a decentralised heat pump hot water system as a proxy for a centralised system only when all the following conditions are met: 

   - a. A centralised heat pump hot water system is used in the building, (i.e. the proxy is not available where another central hot water technology is used, like gas instant or storage or electric instant) 

   - b. The system operates on a continuous tariff, not off-peak 

   - c. The building serviced by the centralised heat pump is four storeys or more 

   - d. A closed loop piping system (circulatory) is in place, (i.e. not reticulated) 

   - e. The pipe insulation used is in accordance with the minimum NCC/BCA pipe insulation requirements and 


- 12.12 Where the conditions above are met for the project, the proxy operates by modelling a decentralised heat pump hot water, on a continuous tariff, in each sole 

OFFICIAL 


OFFICIAL 


occupancy unit of the building to represent the central heat pump hot water system. The Small Technology Certificate values in Table 12 are to be entered in the software based on the specified CER heat pump locations. 


|Location|**Model the following decentralised**<br>**system**|
|---|---|
|CER heat pump Zone 3<br>(including Adelaide, Brisbane and Perth)|Heat pump, 25 STC, continuous|
|CER heat pump Zone 4 and 5<br>(including Melbourne and Canberra)|Heat pump, 27 STC, continuous|



- 12.13 When using this proxy, the assessor must make the relevant certifying authority aware that the model underpinning compliance is different to what is being constructed. The assessor must add the following text in the ‘additional notes’: 

This system is a proxy for the centralised heat pump system that will be installed. It is included for modelling purposes only. The proxy conditions are: 

   - _A centralised heat pump hot water system is used in the building._ 

   - _The system operates on a continuous tariff._ 

   - _The building serviced by the centralised heat pump is four storeys or more._ 

   - _A closed loop piping system (circulatory) is in place, not reticulated._ 

   - _The pipe insulation used is in accordance with minimum NCC/BCA pipe insulation requirements._ 

   - _The project is in CER heat pump zones 3, 4 or 5._ 

- 12.14 All other apartment centralised hot water types are currently excluded, this clause only covers heat pump hot water systems, other centralised hot water and heating and cooling technologies will be incorporated in future iterations of NatHERS Whole of Home. 

## **Plug loads and cooking loads** 

- 12.15 Assessors must enter the energy source(s) of cooking appliances. 

- 12.16 If energy source(s) for cooking appliances are not specified then apply the defaults set out in Table 10 and note in the ‘additional notes’ field of the NatHERS Certificate. 

## **Lighting** 

- 12.17 Assessors must enter the indoor lighting power density (W/m[2] ) in the design documentation. If unknown, apply the default value of 5 W/m[2] . 

OFFICIAL 


OFFICIAL 



## **Pools and spas** 

- 12.18 Pool and spa heating is not modelled under NCC 2022. 

- 12.19 Pools 

A pool is a water-retaining structure designed for human use, holds more than 680 litres of water and incorporates, or is connected to, equipment capable of filtering and/or heating the water. It includes any waterslide, wave pool, hydrotherapy pool or other similar structures. Assessors must enter: 

   - a. volume – if this is unknown, enter the surface area 

   - b. pump type – if unknown, use defaults in Table 10 

   - c. star rating (2019 GEMS determination) – if unknown, use defaults in Table 10. 

- 12.20 Spas 

Spas are currently modelled as for pools. 

## **On-site renewable energy** 

- 12.21 Only solar photovoltaic (PV) systems are included in Whole of Home calculations. Assessors must enter size, inclination, and direction of arrays and inverter capacity as provided in the design documentation. The size of the PV system must be known otherwise it cannot be included. Where other values are unknown, apply the defaults provided in Table 10. These must be noted in the ‘additional notes’ field of the NatHERS Certificate. 

- 12.22 Where PV arrays are located on multiple orientations and inclinations, each array must be entered separately. 

- 12.23 NatHERS currently cannot specify a class 1 microgrid or centralised PV systems for Class 2 buildings or Class 4 parts of a building. 

## **On-site energy storage** 

- 12.24 Assessors must enter the battery technology type and size provided in the design documentation. Where battery technology type and size are not known, the energy storage cannot be included. 

- 12.25 NatHERS allows the use of lithium-Ion, lead acid and zinc bromine battery types. Other battery types are currently not included in NatHERS software and therefore cannot be included in the assessment. 

OFFICIAL 


OFFICIAL **Version 20241023 For use with Chenath 3.22 and 3.23** 

## **What changes require a Whole of Home re-rating?** 

- 12.26 As with NatHERS thermal assessments, when the specifications of a project change, the Whole of Home assessment must be revised for any of the following changes: 

   - a. there is a change in the technology, efficiency or fuel type for any of the appliances or systems 

   - b. the NatHERS thermal assessment is updated. 

   - c. if the value of small-scale technology certificates (STCs) of selected hot water system has decreased OR increased beyond the substitution range noted in the certificate. 

   - d. pool volume is increased. 

## 13. Finishing the assessment 

## **Stamping requirements** 

- 13.1 Before stamping the design documentation with the NatHERS QR code stamp (previously referred to as a mini-certificate) and producing a final NatHERS Certificate, the assessor must: 

   - a. confirm all requirements detailed in this Technical Note have been met 

   - b. confirm the information in the assessment aligns with the design documentation and 

   - c. ensure all defaults, substitutions, assumptions, conflicts and justifications are noted in the ‘additional notes’ section of the NatHERS Certificate. 

- 13.2 The NatHERS QR code stamp must be added electronically to all design documentation that is relevant to the NatHERS assessment. This may include but is not limited to: 

   - a. site and floor plans 



   - d. window, skylight and door schedules 


   - f. electrical plans including lighting and mechanical ventilation 

   - g. insulation information (e.g. contained within construction drawings) where provided 


OFFICIAL 


OFFICIAL 



- i. any design amendments and 


The stamp should not obscure any information on the design documentation or the mark of any other practitioner. 

- 13.3 Accredited assessors must include their AAO stamp if required by their AAO (generally below the NatHERS stamp). This stamp must be smaller than the NatHERS stamp. 

- 13.4 For Class 2 dwellings, the NatHERS Class 2 summary QR code stamp is to be stamped on each page of the documentation that is relevant to the NatHERS assessment (see 13.2 above). 

## **Final Documentation – NatHERS Certificate** 

- 13.5 The assessor must supply the client with the NatHERS Certificate and the stamped design documentation as outlined in 13.2 and Table 1. 

- 13.6 A Class 1b dwelling with a design layout approximating that of a house with multiple bedrooms and a shared kitchen, living and bathroom spaces and < 300m[2] must use the single dwelling NatHERS Certificate. 

- 13.7 A Class 1b dwelling that is four or more single dwellings on a single allotment, or a Class 1b dwelling with kitchenettes in each bedroom, where each bedroom ‘unit’ is being modelled as an individual Class 1a, must use the Class 1 NatHERS Summary Certificate. Each individual dwelling or ‘unit’ must have an individual NatHERS Certificate. 

- 13.8 For Class 2 dwellings, each unit must have an individual NatHERS Certificate and the entire building must have a summary NatHERS Certificate with an average NatHERS thermal performance rating. 

   - 13.8.1 Where a Whole of Home assessment has been conducted for the dwelling, the summary NatHERS Certificate will show the lowest individual Whole of Home rating for a dwelling in the entire building. If none of the dwellings in the building are assessed under Whole of Home, the summary certificate will not show a Whole of Home rating. 

   - 13.8.2 Where a number of Class 2 multi-unit buildings are located in close physical proximity as part of the same development, or where the strata plan identifies separate lots, a Class 2 summary certificate must be completed for each building/lot separately. 

   - 13.8.3 At the request of a client, a single Class 2 summary certificate can be produced for buildings that are combined and share a lot (for example, by a bridge, shared underground space or an enclosed walkway) where NCC requirements for combined buildings are met. 

OFFICIAL 


OFFICIAL 



## 14. Definitions 

|Term / acronym|Definition|
|---|---|
|AAO|Assessor Accrediting Organisation|
|ACOP|annual coefficient of performance|
|AEER|annual energy efficiency ratio|
|BASIX|An integrated part of the NSW planning system, Building Sustainability Index<br>(BASIX) is implemented under the_Environmental Planning and Assessment Act_<br>_1979_. BASIX applies to all residential dwelling types and is part of the Development<br>Application process in NSW.|
|CER|Clean Energy Regulator|
|Chenath|The calculation engine developed by CSIRO that predicts annual totals of hourly<br>heating and cooling energy requirements for residential buildings. It underpins the<br>user interface software tools including AccuRate, HERO, FirstRate5 and BERS.<br>Chenath 3.22 applies NCC2022 but does not include WERSlink (access to the<br>windows library at the Australian Glazing and Windows Association.<br>Chenath 3.23 also applies NCC 2022 and includes WERSlink.|
|Dark colour|Solar absorptance = 0.85|
|Design documentation|Everything that supports the NatHERS rating and certificate, e.g. plans, lighting<br>schedule, window schedule, emails clarifying specifications, etc.|
|Energy value|The net cost to society including, but not limited to, costs to the building user, the<br>environment and energy networks (as defined in the ABCB Housing Provisions<br>Standard).|
|GEMS|Greenhouse and Energy Minimum Standards (national)|
|HSPF|Heating seasonal performance factor|
|Kitchenette|A facility that provides:<br>•<br>a sink, defined by the NCC as a means for rinsing, washing food and<br>utensils and disposal of the associated wastewater<br>•<br>a means to cook or heat food (inbuilt or plugin)<br>•<br>a food preparation area/bench and<br>•<br>a means to keep food cold, i.e. a fridge space|
|Light colour|Solar absorptance = 0.3|
|Medium colour|Solar absorptance = 0.5|
|Main appliance|The main heating or cooling equipment is that which serves at least 70% of the<br>conditioned zone. If no single heating and cooling equipment serves at least 70%, it<br>is the equipment that results in the highest energy consumption. This may require<br>multiple simulations to determine.|
|Multi-split|A multi-split system air conditioner has one outdoor compressor unit with multiple<br>indoor units which can be individually controlled.|
|NatHERS software tool|NatHERS accredited software tools which can be used, in regulation mode, to<br>generate ratings for regulatory purposes.|
|NatHERS assessment|This includes either or both the thermal assessment and Whole of Home<br>assessment.|



OFFICIAL 


OFFICIAL 



|Parent zone|The parent zone is the larger zone that the smaller space is accessed from. E.g. a<br>pantry’s parent zone may be the kitchen/living zone.|
|---|---|
|Rating|This includes the thermal assessment or Whole of Home assessment (or both).|
|Reverse cycle fixed<br>capacity|Includes single-speed compressor, a 2-speed compressor and a 2-stage capacity<br>unit|
|Reverse cycle variable<br>capacity|Includes multistage capacity and variable capacity units (usually inverter driven)|
|RTO|Registered Training Organisations|
|Solar absorptance|This is the fraction of solar radiation being absorbed by a surface.<br>Solar absorptance = 1 – solar reflectance.|
|Solar reflectance|This is the fraction of solar radiation being reflected from a surface.<br>Solar reflectance = 1 – solar absorptance.|
|STC|Small-scale technology certificate|
|TCSPF|Total cooling seasonal performance factor|
|Ventilated|Refers to the presence of controllable openings including windows, roof windows<br>and doors|



OFFICIAL 


OFFICIAL 



## Appendix 1:  Zoning in NatHERS 

Situations may arise in unconventional dwelling designs where more than one zone option is possible. In the absence of definitive advice from an AAO or the NatHERS Administrator, the Assessor may need to use discretion, considering for example the **intent** of the zone, including consulting with their relevant certifier. In such circumstances the Assessor must document their decisions for later review and quality assurance. 

|**Spaces/ areas**<br>_Ventilated:_<br>_has a door and or an openable window_<br>_on an external wall or roof_<br>_Unventilated:  has neither an openable window nor_<br>_door on an external wall_||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||Zones||||||||
|||||||||||**Class 2 or 4**<br>**only**||
||Kitchen / living1|Living2|Day-time|Bedroom|Night time|Unconditioned3|**Refer to the parent**<br>**zone**|Garage - unconditioned|Garage - conditioned|Glazed common area|**Shared basement car**<br>**park**|
|Airlock4|||⚫|||⚫||||||
|Bathroom see flowchart Appendix 2||||||||||||
|Bedroom||||⚫||||||||
|Cellar,conditioned|||⚫|||||||||
|Cellar,unconditioned||||||⚫||||||
|Corridor within a dwelling– see “Hallway”|||⚫|||||||||
|Corridor adjacent to apartment, public,unconditioned, glazed||||||||||⚫||
|Diningroom2||⚫|⚫|||||||||
|Ensuite – see flowchart Appendix 2||||||||||||
|Familyroom2||⚫|⚫|||||||||
|Garage,conditioned|||||||||⚫|||
|Garage,unconditioned||||||||⚫||||
|Gym|||⚫|||||||||
|Hallway,cannot be closed off from the zone it originates from|||⚫|||||||||
|Hallway, solely associated with a bedroom complex5that can be closed off<br>from the zone it originates from|||||||⚫|||||
|Kitchen(main)with or without meals/lounge/living/dining|⚫|||||||||||
|Kitchen(second) /kitchenette||⚫||||||||||
|Laundry,unventilated|||||||⚫|||||
|Laundry,ventilated with door to another zone||||||⚫||||||
|Laundry,ventilated open to another zone|||||||⚫|||||
|Lift|||⚫|||||||||
|Living2||⚫|⚫|||||||||
|Lounge2||⚫|⚫|||||||||
|Media2||⚫|⚫|||||||||
|Outdoor livingarea,capable of beingfullyenclosed and conditioned|||⚫|||||||||
|Pantry,not walk-in|||||||⚫|||||
|Pantry,walk-in|||⚫|||||||||
|Parents’ retreat|||||⚫|||||||
|Pool room|||⚫|||||||||
|Powder room,unventilated|||||||⚫|||||
|Powder room,ventilated||||||⚫||||||
|Rumpus2||⚫|⚫|||||||||
|Sauna|||⚫|||||||||
|Shared basement**carpark**enclosed|||||||||||⚫|
|Small spaces,not walk-in|||||||⚫|||||
|Storage|||||||⚫|||||
|Storage under staircase|||||||⚫|||||
|Studyor office with either built-in wardrobe,WIR or ensuite||||⚫||||||||
|Studyor office without either built-in wardrobe,WIR or ensuite|||⚫|||||||||
|Theatre,library, prayer room2||⚫|⚫|||||||||
|Voids e.g. wall, plumbing,service ducts|||||||⚫|||||
|Walk-in-robe(WIR)|||||⚫|||||||
|WC,unventilated|||||||⚫|||||
|WC,ventilated||||||⚫||||||



> 1 All dwellings must contain only one main kitchen/living zone. All additional smaller kitchens/kitchenettes within the dwelling must be zoned as “living”. 

> 2 If there are more than two living areas (excluding kitchen/living), then: a) the two largest living areas are zoned as “living” and b) the other areas are zoned as “daytime”. 

> 3 Every dwelling must have at least one unconditioned zone. If no rooms fit the definition of “unconditioned’, then choose the smallest zone and model this as “unconditioned”. 

> 4 An airlock must have: 

a) an external door and or openable window on an external wall and b) one or more internal doors, of which, only one opens to a conditioned zone.  If it does not meet these two criteria it must be zoned as “daytime”. 

> 5 A single bedroom (usually the master bedroom) with exclusive ensuite and/or walk in robe, or, a cluster of secondary bedrooms, which may be linked by an exclusive hallway which can be closed off from the zone it originates from. 

OFFICIAL 


OFFICIAL 






In-floor heating?<br>yes no<br>Only bathroom in<br>dwelling?<br>yes (1) (2)  no<br>Associated with<br>Ventilated? bedroom. NOT for<br>general use in dwelling<br>ventilated?<br>yes no yes no<br>Does room have closable<br>yes no door?<br>yes no<br>Night time Parent zone Unconditioned Parent zone Parent zone Night time<br>1 This means that there is no other bathroom or WC for general household use<br>2         Every dwelling must have at least one unconditioned<br>zone.<br>


OFFICIAL 


