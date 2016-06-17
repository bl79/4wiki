/**
 * Created by Bladislav on 05.06.2016.
 */
// document.editform.wpTextbox1.value = "{";
// Make sure the utilities module is loaded (will only load if not already)
mw.loader.using( 'mediawiki.util', function () {

    // Wait for the page to be parsed
    $(document).ready( function () {

        // document.editform.wpTextbox1.value = "{";
   //see below "Portlets" subsection
   //      var link = mw.util.addPortletLink( 'p-cactions', '#', 'Wikify', 'ca-wikify', 'Mark for wikification');
   //      $( link ).click( function ( event ) {
   //          event.preventDefault();
            doQwikify();

        // } );
    } );
} );

function doQwikify() {
    // mw.util.jsMessage( 'The selected text is "' + mw.html.escape( $( '#wpTextbox1' ).textSelection( 'getSelection' ) ) + '".' );
    // document.editform.wpTextbox1.value = "{" + "{wikify}}\n\n" + document.editform.wpTextbox1.value;
    // document.editform.submit();
}