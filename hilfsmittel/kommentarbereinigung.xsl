<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs tei" version="2.0">



    <xsl:template name="langIt" match='//tei:hi[@rend = "color(#000000)italic"]'>
        <lang xml:lang="ar-Latn">
            <xsl:value-of select="."/>
        </lang>
    </xsl:template>

    <xsl:template match="//tei:p">

        <p>
            <!-- 
            <xsl:call-template name="langIt" />
            -->
            <xsl:apply-templates/>
        </p>
    </xsl:template>

</xsl:stylesheet>
