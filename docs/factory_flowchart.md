# PedalWorks Master Factory Flowchart

The diagram below traces one unit of work through the entire PedalWorks
factory: from the five outside suppliers, through intake, scheduling,
procurement and assembly, quality (with its rework loop), and out through
shipping. Finance and the Ledger sit apart at the bottom, because every
stage above posts a cost to the Ledger rather than sitting in the linear
path.

```
                                                        Suppliers                                                         
+--------------------+   +--------------------+   +--------------------+   +--------------------+   +--------------------+
|   FrameForge Ltd   |   |    RollRight Co    |   |   GearWorks Inc    |   |   BrakeSafe GmbH   |   |   ForkFactory Co   |
+--------------------+   +--------------------+   +--------------------+   +--------------------+   +--------------------+
         |                      |                      |                      |                      |          
      supplies               supplies               supplies               supplies               supplies      
         v                      v                      v                      v                      v          
+--------------------+   +--------------------+   +--------------------+   +--------------------+   +--------------------+
|       Frame        |   |      Wheelset      |   |     Drivetrain     |   |     Brake Set      |   |  Suspension Fork   |
+--------------------+   +--------------------+   +--------------------+   +--------------------+   +--------------------+
         |                      |                      |                      |                      |          
         v                      v                      v                      v                      v          
                                                            v                                                             
                     +------------------------------------------------------------------------------+
                     |                            North Intake Warehouse                            |
                     |           (receives incoming parts from all five suppliers above)            |
                     +------------------------------------------------------------------------------+
                                                            |                                                             
                                                            v                                                             
                     +------------------------------------------------------------------------------+
                     |                          Scheduler   (fan-out hub)                           |
                     |                      reads PartsDB   --   reads OrderDB                      |
                     |   releases_to Assembly directly, in addition to the Procurement path below   |
                     +------------------------------------------------------------------------------+
                                       |                                     |               
                                    triggers                                                 
                                       v                                     v               
                         +------------------------------+        +------------------------------+
                         |         Procurement          |        |          Inventory           |
                         +------------------------------+        +------------------------------+
                                       |                                     |               
                                         +---------------------------------------+               
                                                             v
                     +------------------------------------------------------------------------------+
                     |                     Portland Assembly Floor   (Assembly)                     |<---------+
                     +------------------------------------------------------------------------------+          |
                                                             |          |
                                                             v          |   rework: a failed Quality check returns_to Assembly
                     +------------------------------------------------------------------------------+          |
                     |                                   Quality                                    |----------+
                     +------------------------------------------------------------------------------+
                                                             |
                                                             v
                     +------------------------------------------------------------------------------+
                     |                          South Distribution Center                           |
                     |                                  (Shipping)                                  |
                     +------------------------------------------------------------------------------+

                                 Assembly also produces the two finished bicycle models:                                  
                                                                                                            
                                       |                                     |               
                                    produces                              produces           
                                       v                                     v               
                         +------------------------------+        +------------------------------+
                         |         City Cruiser         |        |         Trail Blazer         |
                         +------------------------------+        +------------------------------+
                                                                 +-- used_in: Frame, Wheelset, and Suspension Fork all feed into Trail Blazer

==========================================================================================================================
|                                       Finance / Ledger  (persisted in LedgerDB)                                        |
|                                            Procurement posts_cost_to Ledger                                            |
|                                             Assembly posts_cost_to Ledger                                              |
|                                              Quality posts_cost_to Ledger                                              |
|                                             Shipping posts_cost_to Ledger                                              |
|                                 Ledger is the one place all factory spending converges                                 |
==========================================================================================================================
```

Every box above corresponds to a stage, hub, warehouse, part,
supplier, or system named in the PedalWorks data model. PartsDB and
OrderDB back the Scheduler's read side; LedgerDB backs every posted
cost. The rework loop is the only cycle in the graph: a failed Quality
check returns the unit to Assembly instead of continuing on to Shipping.
