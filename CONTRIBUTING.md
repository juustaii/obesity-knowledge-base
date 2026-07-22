# Contributing Guidelines

## Adding Materials

### Guidelines
Place official clinical guidelines in `guidelines/` folder with naming convention:
```
guidelines/[ORGANIZATION]_[YEAR]_[TITLE].pdf
```
Example: `guidelines/WHO_2023_Obesity_Management.pdf`

### Articles
Add peer-reviewed articles to `articles/` with:
```
articles/[YEAR]_[FIRST_AUTHOR]_[SHORT_TITLE].pdf
```
Example: `articles/2023_Smith_GLP1_Efficacy.pdf`

### Clinical Trials
Add trial data as markdown or JSON to `trials/`:
```
trials/[TRIAL_ID]_[BRIEF_NAME].md
```

## Metadata

Include a metadata file for each addition:
```json
{
  "title": "Article Title",
  "authors": ["Author 1", "Author 2"],
  "year": 2023,
  "source": "Journal Name",
  "doi": "10.xxxx/xxxxx",
  "abstract": "Brief summary...",
  "keywords": ["obesity", "treatment", "trial"]
}
```

## Removal

To remove outdated or duplicate materials:
1. Create an issue documenting why
2. Update CRAWLER_LOG.md
3. Delete file and commit with reference to issue

## Updating Crawler Config

Modify `crawler-config/` files to adjust:
- Search keywords
- Data sources
- Relevance thresholds
- Exclusion criteria

Changes take effect on next crawler run cycle.