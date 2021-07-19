{% snapshot std_snapshot %}

{{
    config(
      target_database='studentinfo',
      target_schema='studentinfo',
      unique_key='SNO',

      strategy='timestamp',
      updated_at='SNO',
    )
}}

select * from {{ ref('studentdatastd') }}

{% endsnapshot %}