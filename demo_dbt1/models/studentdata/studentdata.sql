 with source_std as (
    select *
    from {{ source('studentdata', 'std') }}
 ),
 final  as (
         select *
         from source_std
 )
 select * from final