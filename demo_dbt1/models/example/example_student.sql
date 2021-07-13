 with studentdata as (
       select * from {{ref('studentdata')}}

 ),
 locations as (
     select * from {{ref('locations')}}
 ),

 final as(
     select
        studentdata.name
        locations.city
        locations.state
     from locations
     left join studentdata
         on locations.name = studentdata.name
 )
 select * from final