<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl" version="1.0">
  <xsl:template match="/">
    <!-- Ouvrir le répertoire -->
    <xsl:variable name="dir" select="php:function('opendir', '.')"/>
    
    <!-- Appels explicites à readdir() -->
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    <xsl:value-of select="php:function('readdir')"/><br/>file : <br/>
    
    <!-- Fermer le répertoire -->
    <xsl:value-of select="php:function('closedir')"/>

  </xsl:template>
</xsl:stylesheet>
