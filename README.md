# Ps4_popgen
Comp_tools problemSet4 on data source with an API
The GBIF (Global Biodiversity Information Facility) API allows users to programmatically access various biodiversity datasets, including species occurrences, taxonomic information, maps, and related literature. In this example, the Literature API was used to fetch peer-reviewed publications that reference GBIF datasets, downloads, or cite biodiversity data in general.

The request retrieves a JSON response that includes metadata such as:

Authors: Names of individuals who contributed to the publication.
Countries of Research: Geographical regions relevant to the study.
Published Date: The publication date.
GBIF Relevance: How the study interacts with GBIF data (e.g., cited, mentioned).
Publisher: The journal or institution where the article was published.
Abstract: A summary of the study's objectives and findings.
Tags and Topics: Categories and keywords related to the article.
DOI/Website: Links to the full publication.

