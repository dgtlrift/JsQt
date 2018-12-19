/* ************************************************************************

   Copyright:

   License:

   Authors:

************************************************************************ */

/**
 * This is the main application class of your custom application "test_class_path"
 *
 * @asset(com/myorg/test_class_path/*)
 */
qx.Class.define("com.myorg.test_class_path.Application",
{
  extend : qx.application.Standalone,



  /*
  *****************************************************************************
     MEMBERS
  *****************************************************************************
  */

  members :
  {
    /**
     * This method contains the initial application code and gets called 
     * during startup of the application
     * 
     * @lint ignoreDeprecated(alert)
     */
    main : function()
    {
      // Call super class
      this.base(arguments);

      // Enable logging in debug variant
      if (qx.core.Environment.get("qx.debug"))
      {
        // support native logging capabilities, e.g. Firebug for Firefox
        qx.log.appender.Native;
        // support additional cross-browser console. Press F7 to toggle visibility
        qx.log.appender.Console;
      }

      /*
      -------------------------------------------------------------------------
        Below is your actual application code...
      -------------------------------------------------------------------------
      */
      // Create the implimentation of Test
      var sample = new com.myorg.test_class_path.impl.Test();

      // Document is the application root
      var doc = this.getRoot();


      // Add Sample Test to document at fixed coordinates
      doc.add(sample.getWidget(), {edge: 0});
    }
  }
});
