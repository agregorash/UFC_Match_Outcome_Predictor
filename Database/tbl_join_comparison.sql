-- Create a view in order to save data storage
-- Left Join the two tables in order to show a comparison of "tale of the tape" 
-- stats vs the stats we found to correlate to wins most

CREATE VIEW fighter_comparison AS
SELECT original."R_fighter", original."B_fighter", original."gender", original."R_age", original."B_age", original."R_Height_cms", original."B_Height_cms", original."R_Weight_lbs", original."B_Weight_lbs", original."R_Reach_cms", original."B_Reach_cms", master."sig_str_landed_bout_diff", master."ev_diff", master."odds_diff", master."tot_str_landed_bout_diff", master."sig_str_pct_bout_diff"
FROM original
LEFT JOIN master ON original.index = master.index
;