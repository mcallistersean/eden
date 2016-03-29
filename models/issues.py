tablename = "issues_issue"

db.define_table(
    tablename,
    Field(
        "name",
        label=T("Name")
    ),
    s3db.pr_person_id(
        label=T("Issuer")
    ),
    *s3_meta_fields()
)
