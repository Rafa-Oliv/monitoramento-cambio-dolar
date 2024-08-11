﻿import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class BookmarksOutlineLevelCollection:
    """A collection of individual bookmarks outline level.
    To learn more, visit the `Working with Bookmarks <https://docs.aspose.com/words/python-net/working-with-bookmarks/>` documentation article.
    
    Key is a case-insensitive string bookmark name. Value is a int bookmark outline level.
    
    Bookmark outline level may be a value from 0 to 9. Specify 0 and Word bookmark will not be displayed in the document outline.
    Specify 1 and Word bookmark will be displayed in the document outline at level 1; 2 for level 2 and so on."""
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> int:
        """Gets or sets a bookmark outline level at the specified index.
        
        :param index: Zero-based index of the bookmark.
        :returns: The outline level of the bookmark. Valid range is 0 to 9."""
        ...
    
    def __setitem__(self, index: int, value: int):
        ...
    
    def get_by_name(self, name: str) -> int:
        """Gets or a sets a bookmark outline level by the bookmark name."""
        ...
    
    def add(self, name: str, outline_level: int) -> None:
        """Adds a bookmark to the collection.
        
        :param name: The case-insensitive name of the bookmark to add.
        :param outline_level: The outline level of the bookmark. Valid range is 0 to 9."""
        ...
    
    def contains(self, name: str) -> bool:
        """Determines whether the collection contains a bookmark with the given name.
        
        :param name: Case-insensitive name of the bookmark to locate.
        :returns: ``True`` if item is found in the collection; otherwise, ``False``."""
        ...
    
    def index_of_key(self, name: str) -> int:
        """Returns the zero-based index of the specified bookmark in the collection.
        
        :param name: The case-insensitive name of the bookmark.
        :returns: The zero based index. Negative value if not found."""
        ...
    
    def remove(self, name: str) -> None:
        """Removes a bookmark with the specified name from the collection.
        
        :param name: The case-insensitive name of the bookmark."""
        ...
    
    def remove_at(self, index: int) -> None:
        """Removes a bookmark at the specified index.
        
        :param index: The zero based index."""
        ...
    
    def clear(self) -> None:
        """Removes all elements from the collection."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of elements contained in the collection."""
        ...
    
    ...

class CssSavingArgs:
    """Provides data for the :meth:`ICssSavingCallback.css_saving` event.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article.
    
    By default, when Aspose.Words saves a document to HTML, it saves CSS information inline
    (as a value of the **style** attribute on every element).
    
    :class:`CssSavingArgs` allows to save CSS information into file by providing your own stream object.
    
    To save CSS into stream, use the :attr:`CssSavingArgs.css_stream` property.
    
    To suppress saving CSS into a file and embedding to HTML document use the :attr:`CssSavingArgs.is_export_needed` property."""
    
    @property
    def document(self) -> aspose.words.Document:
        """Gets the document object that is currently being saved."""
        ...
    
    @property
    def keep_css_stream_open(self) -> bool:
        """Specifies whether Aspose.Words should keep the stream open or close it after saving an CSS information.
        
        Default is ``False`` and Aspose.Words will close the stream you provided
        in the :attr:`CssSavingArgs.css_stream` property after writing an CSS information into it.
        Specify ``True`` to keep the stream open."""
        ...
    
    @keep_css_stream_open.setter
    def keep_css_stream_open(self, value: bool):
        ...
    
    @property
    def css_stream(self) -> io.BytesIO:
        """Allows to specify the stream where the CSS information will be saved to.
        
        This property allows you to save CSS information to a stream.
        
        The default value is ``None``. This property doesn't suppress saving CSS information to a file or
        embedding to HTML document. To suppress exporting CSS use the :attr:`CssSavingArgs.is_export_needed` property.
        
        Using :class:`ICssSavingCallback` you cannot substitute CSS with
        another. It is intended only for saving CSS to a stream."""
        ...
    
    @css_stream.setter
    def css_stream(self, value: io.BytesIO):
        ...
    
    @property
    def is_export_needed(self) -> bool:
        """Allows to specify whether the CSS will be exported to file and embedded to HTML document. Default is ``True``.
        When this property is ``False``, the CSS information will not be saved to a CSS file and will not be embedded to HTML document."""
        ...
    
    @is_export_needed.setter
    def is_export_needed(self, value: bool):
        ...
    
    ...

class DigitalSignatureDetails:
    """Contains details for signing a document with a digital signature."""
    
    def __init__(self, certificate_holder: aspose.words.digitalsignatures.CertificateHolder, sign_options: aspose.words.digitalsignatures.SignOptions):
        """Initializes a new instance of :class:`DigitalSignatureDetails` class.
        
        :param certificate_holder: A certificate holder which contains the certificate itself.
        :param sign_options: Signature options to use for signing a document."""
        ...
    
    @property
    def certificate_holder(self) -> aspose.words.digitalsignatures.CertificateHolder:
        """Gets or sets a :attr:`DigitalSignatureDetails.certificate_holder` object that contains the certificate used to sign a document."""
        ...
    
    @certificate_holder.setter
    def certificate_holder(self, value: aspose.words.digitalsignatures.CertificateHolder):
        ...
    
    @property
    def sign_options(self) -> aspose.words.digitalsignatures.SignOptions:
        """Gets or sets a :attr:`DigitalSignatureDetails.sign_options` object used to sign a document."""
        ...
    
    @sign_options.setter
    def sign_options(self, value: aspose.words.digitalsignatures.SignOptions):
        ...
    
    ...

class DocSaveOptions(aspose.words.saving.SaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.DOC` or
    :attr:`aspose.words.SaveFormat.DOT` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article.
    
    At the moment provides only the :attr:`DocSaveOptions.save_format` property, but in the future will have
    other options added, such as an encryption password or digital signature settings."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.DOC` format."""
        ...
    
    @overload
    def __init__(self, save_format: aspose.words.SaveFormat):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.DOC` or
        :attr:`aspose.words.SaveFormat.DOT` format.
        
        :param save_format: Can be :attr:`aspose.words.SaveFormat.DOC` or :attr:`aspose.words.SaveFormat.DOT`."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can be :attr:`aspose.words.SaveFormat.DOC` or :attr:`aspose.words.SaveFormat.DOT`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def password(self) -> str:
        """Gets/sets a password to encrypt document using RC4 encryption method.
        
        In order to save document without encryption this property should be ``None`` or empty string."""
        ...
    
    @password.setter
    def password(self, value: str):
        ...
    
    @property
    def save_routing_slip(self) -> bool:
        """When ``False``, RoutingSlip data is not saved to output document.
        Default value is ``True``."""
        ...
    
    @save_routing_slip.setter
    def save_routing_slip(self, value: bool):
        ...
    
    @property
    def always_compress_metafiles(self) -> bool:
        """When ``False``, small metafiles are not compressed for performance reason.
        Default value is ``True``, all metafiles are compressed regardless of its size."""
        ...
    
    @always_compress_metafiles.setter
    def always_compress_metafiles(self, value: bool):
        ...
    
    @property
    def save_picture_bullet(self) -> bool:
        """When ``False``, PictureBullet data is not saved to output document.
        Default value is ``True``.
        
        This option is provided for Word 97, which cannot work correctly with PictureBullet data.
        To remove PictureBullet data, set the option to "false"."""
        ...
    
    @save_picture_bullet.setter
    def save_picture_bullet(self, value: bool):
        ...
    
    @property
    def digital_signature_details(self) -> aspose.words.saving.DigitalSignatureDetails:
        """Gets or sets :class:`DigitalSignatureDetails` object used to sign a document."""
        ...
    
    @digital_signature_details.setter
    def digital_signature_details(self, value: aspose.words.saving.DigitalSignatureDetails):
        ...
    
    ...

class DocumentPartSavingArgs:
    """Provides data for the :meth:`IDocumentPartSavingCallback.document_part_saving` callback.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article.
    
    When Aspose.Words saves a document to HTML or related formats and :attr:`HtmlSaveOptions.document_split_criteria`
    is specified, the document is split into parts and by default, each document part is saved into a separate file.
    
    Class :class:`DocumentPartSavingArgs` allows you to control how each document part will be saved.
    It allows to redefine how file names are generated or to completely circumvent saving of document parts into
    files by providing your own stream objects.
    
    To save document parts into streams instead of files, use the :attr:`DocumentPartSavingArgs.document_part_stream` property."""
    
    @property
    def document(self) -> aspose.words.Document:
        """Gets the document object that is being saved."""
        ...
    
    @property
    def document_part_file_name(self) -> str:
        """Gets or sets the file name (without path) where the document part will be saved to.
        
        This property allows you to redefine how the document part file names are generated
        during export to HTML or EPUB.
        
        When the callback is invoked, this property contains the file name that was generated
        by Aspose.Words. You can change the value of this property to save the document part into a
        different file. Note that the file name for each part must be unique.
        
        :attr:`DocumentPartSavingArgs.document_part_file_name` must contain only the file name without the path.
        Aspose.Words determines the path for saving using the document file name. If output document
        file name was not specified, for instance when saving to a stream, this file name is used only
        for referencing document parts. The same is true when saving to EPUB format."""
        ...
    
    @document_part_file_name.setter
    def document_part_file_name(self, value: str):
        ...
    
    @property
    def keep_document_part_stream_open(self) -> bool:
        """Specifies whether Aspose.Words should keep the stream open or close it after saving a document part.
        
        Default is ``False`` and Aspose.Words will close the stream you provided
        in the :attr:`DocumentPartSavingArgs.document_part_stream` property after writing a document part into it.
        Specify ``True`` to keep the stream open. Please note that the main output stream
        provided in the call to :meth:`aspose.words.Document.save` or
        :meth:`aspose.words.Document.save` will never be closed by Aspose.Words
        even if :attr:`DocumentPartSavingArgs.keep_document_part_stream_open` is set to ``False``."""
        ...
    
    @keep_document_part_stream_open.setter
    def keep_document_part_stream_open(self, value: bool):
        ...
    
    @property
    def document_part_stream(self) -> io.BytesIO:
        """Allows to specify the stream where the document part will be saved to.
        
        This property allows you to save document parts to streams instead of files during HTML export.
        
        The default value is ``None``. When this property is ``None``, the document part
        will be saved to a file specified in the :attr:`DocumentPartSavingArgs.document_part_file_name` property.
        
        When saving to a stream in HTML format is requested by :meth:`aspose.words.Document.save`
        or :meth:`aspose.words.Document.save` and first document part is about to be saved,
        Aspose.Words suggests here the main output stream initially passed by the caller.
        
        When saving to EPUB format that is a container format based on HTML, :attr:`DocumentPartSavingArgs.document_part_stream` cannot
        be specified because all subsidiary parts will be encapsulated into a single output package."""
        ...
    
    @document_part_stream.setter
    def document_part_stream(self, value: io.BytesIO):
        ...
    
    ...

class DocumentSavingArgs:
    """An argument passed into :meth:`IDocumentSavingCallback.notify`.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article."""
    
    @property
    def estimated_progress(self) -> float:
        """Overall estimated percentage progress."""
        ...
    
    ...

class DownsampleOptions:
    """Allows to specify downsample options.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def downsample_images(self) -> bool:
        """Specifies whether images should be downsampled.
        
        The default value is ``True``."""
        ...
    
    @downsample_images.setter
    def downsample_images(self, value: bool):
        ...
    
    @property
    def resolution(self) -> int:
        """Specifies the resolution in pixels per inch which the images should be downsampled to.
        
        The default value is 220 ppi."""
        ...
    
    @resolution.setter
    def resolution(self, value: int):
        ...
    
    @property
    def resolution_threshold(self) -> int:
        """Specifies the threshold resolution in pixels per inch.
        If resolution of an image in the document is less than threshold value,
        the downsampling algorithm will not be applied.
        A value of 0 means the threshold check is not used and all images that can be reduced in size are downsampled.
        
        The default value is 0."""
        ...
    
    @resolution_threshold.setter
    def resolution_threshold(self, value: int):
        ...
    
    ...

class FixedPageSaveOptions(aspose.words.saving.SaveOptions):
    """Contains common options that can be specified when saving a document into fixed page formats (PDF, XPS,
    images etc).
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    @property
    def page_set(self) -> aspose.words.saving.PageSet:
        """Gets or sets the pages to render.
        Default is all the pages in the document."""
        ...
    
    @page_set.setter
    def page_set(self, value: aspose.words.saving.PageSet):
        ...
    
    @property
    def page_saving_callback(self) -> aspose.words.saving.IPageSavingCallback:
        """Allows to control how separate pages are saved when a document is exported to fixed page format."""
        ...
    
    @page_saving_callback.setter
    def page_saving_callback(self, value: aspose.words.saving.IPageSavingCallback):
        ...
    
    @property
    def numeral_format(self) -> aspose.words.saving.NumeralFormat:
        """Gets or sets :class:`NumeralFormat` used for rendering of numerals.
        European numerals are used by default.
        
        If the value of this property is changed and page layout is already built then
        :meth:`aspose.words.Document.update_page_layout` is invoked automatically to update any changes."""
        ...
    
    @numeral_format.setter
    def numeral_format(self, value: aspose.words.saving.NumeralFormat):
        ...
    
    @property
    def metafile_rendering_options(self) -> aspose.words.saving.MetafileRenderingOptions:
        """Allows to specify metafile rendering options."""
        ...
    
    @metafile_rendering_options.setter
    def metafile_rendering_options(self, value: aspose.words.saving.MetafileRenderingOptions):
        ...
    
    @property
    def jpeg_quality(self) -> int:
        """Gets or sets a value determining the quality of the JPEG images inside Html document.
        
        Has effect only when a document contains JPEG images.
        
        Use this property to get or set the quality of the images inside a document when saving in fixed page format.
        The value may vary from 0 to 100 where 0 means worst quality but maximum compression and 100
        means best quality but minimum compression.
        
        The default value is 95."""
        ...
    
    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...
    
    @property
    def color_mode(self) -> aspose.words.saving.ColorMode:
        """Gets or sets a value determining how colors are rendered.
        
        The default value is :attr:`ColorMode.NORMAL`."""
        ...
    
    @color_mode.setter
    def color_mode(self, value: aspose.words.saving.ColorMode):
        ...
    
    @property
    def optimize_output(self) -> bool:
        """Flag indicates whether it is required to optimize output.
        If this flag is set redundant nested canvases and empty canvases are removed,
        also neighbor glyphs with the same formatting are concatenated.
        Note: The accuracy of the content display may be affected if this property is set to ``True``.
        
        Default is ``False``."""
        ...
    
    @optimize_output.setter
    def optimize_output(self, value: bool):
        ...
    
    ...

class FontSavingArgs:
    """Provides data for the :meth:`IFontSavingCallback.font_saving` event.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article.
    
    When Aspose.Words saves a document to HTML or related formats and :attr:`HtmlSaveOptions.export_font_resources`
    is set to ``True``, it saves each font subject for export into a separate file.
    
    :class:`FontSavingArgs` controls whether particular font resource should be exported and how.
    
    :class:`FontSavingArgs` also allows to redefine how font file names are generated or to
    completely circumvent saving of fonts into files by providing your own stream objects.
    
    To decide whether to save a particular font resource, use the :attr:`FontSavingArgs.is_export_needed` property.
    
    To save fonts into streams instead of files, use the :attr:`FontSavingArgs.font_stream` property."""
    
    @property
    def document(self) -> aspose.words.Document:
        """Gets the document object that is being saved."""
        ...
    
    @property
    def font_family_name(self) -> str:
        """Indicates the current font family name."""
        ...
    
    @property
    def bold(self) -> bool:
        """Indicates whether the current font is bold."""
        ...
    
    @property
    def italic(self) -> bool:
        """Indicates whether the current font is italic."""
        ...
    
    @property
    def original_file_name(self) -> str:
        """Gets the original font file name with an extension.
        
        This property contains the original file name of the current font if it is known. Otherwise it can be an empty string."""
        ...
    
    @property
    def original_file_size(self) -> int:
        """Gets the original font file size.
        
        This property contains the original file size of the current font if it is known. Otherwise it can be zero."""
        ...
    
    @property
    def is_export_needed(self) -> bool:
        """Allows to specify whether the current font will be exported as a font resource. Default is ``True``."""
        ...
    
    @is_export_needed.setter
    def is_export_needed(self, value: bool):
        ...
    
    @property
    def is_subsetting_needed(self) -> bool:
        """Allows to specify whether the current font will be subsetted before exporting as a font resource.
        
        Fonts can be exported as complete original font files or subsetted to include only the characters
        that are used in the document. Subsetting allows to reduce the resulting font resource size.
        
        By default, Aspose.Words decides whether to perform subsetting or not by comparing the original font file size
        with the one specified in :attr:`HtmlSaveOptions.font_resources_subsetting_size_threshold`.
        You can override this behavior for individual fonts by setting the :attr:`FontSavingArgs.is_subsetting_needed` property."""
        ...
    
    @is_subsetting_needed.setter
    def is_subsetting_needed(self, value: bool):
        ...
    
    @property
    def font_file_name(self) -> str:
        """Gets or sets the file name (without path) where the font will be saved to.
        
        This property allows you to redefine how the font file names are generated
        during export to HTML.
        
        When the event is fired, this property contains the file name that was generated
        by Aspose.Words. You can change the value of this property to save the font into a
        different file. Note that file names must be unique.
        
        Aspose.Words automatically generates a unique file name for every embedded font when
        exporting to HTML format. How the font file name is generated
        depends on whether you save the document to a file or to a stream.
        
        When saving a document to a file, the generated font file name looks like
        *\<document base file name\>.\<original file name\>\<optional suffix\>.\<extension\>*.
        
        When saving a document to a stream, the generated font file name looks like
        *Aspose.Words.\<document guid\>.\<original file name\>\<optional suffix\>.\<extension\>*.
        
        :attr:`FontSavingArgs.font_file_name` must contain only the file name without the path.
        Aspose.Words determines the path for saving using the document file name,
        the :attr:`HtmlSaveOptions.fonts_folder` and
        :attr:`HtmlSaveOptions.fonts_folder_alias` properties."""
        ...
    
    @font_file_name.setter
    def font_file_name(self, value: str):
        ...
    
    @property
    def keep_font_stream_open(self) -> bool:
        """Specifies whether Aspose.Words should keep the stream open or close it after saving a font.
        
        Default is ``False`` and Aspose.Words will close the stream you provided
        in the :attr:`FontSavingArgs.font_stream` property after writing a font into it.
        Specify ``True`` to keep the stream open."""
        ...
    
    @keep_font_stream_open.setter
    def keep_font_stream_open(self, value: bool):
        ...
    
    @property
    def font_stream(self) -> io.BytesIO:
        """Allows to specify the stream where the font will be saved to.
        
        This property allows you to save fonts to streams instead of files during HTML export.
        
        The default value is ``None``. When this property is ``None``, the font
        will be saved to a file specified in the :attr:`FontSavingArgs.font_file_name` property."""
        ...
    
    @font_stream.setter
    def font_stream(self, value: io.BytesIO):
        ...
    
    ...

class HtmlFixedSaveOptions(aspose.words.saving.FixedPageSaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.HTML_FIXED` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.HTML_FIXED`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def optimize_output(self) -> bool:
        """Flag indicates whether it is required to optimize output.
        If this flag is set redundant nested canvases and empty canvases are removed,
        also neighbor glyphs with the same formating are concatenated.
        Note: The accuracy of the content display may be affected if this property is set to ``True``.
        
        Default is ``True``."""
        ...
    
    @optimize_output.setter
    def optimize_output(self, value: bool):
        ...
    
    @property
    def show_page_border(self) -> bool:
        """Specifies whether border around pages should be shown.
        Default is ``True``."""
        ...
    
    @show_page_border.setter
    def show_page_border(self, value: bool):
        ...
    
    @property
    def page_horizontal_alignment(self) -> aspose.words.saving.HtmlFixedPageHorizontalAlignment:
        """Specifies the horizontal alignment of pages in an HTML document.
        Default value is :attr:`HtmlFixedPageHorizontalAlignment.CENTER`."""
        ...
    
    @page_horizontal_alignment.setter
    def page_horizontal_alignment(self, value: aspose.words.saving.HtmlFixedPageHorizontalAlignment):
        ...
    
    @property
    def page_margins(self) -> float:
        """Specifies the margins around pages in an HTML document.
        The margins value is measured in points and should be equal to or greater than 0.
        Default value is 10 points.
        
        Depends on the value of :attr:`HtmlFixedSaveOptions.page_horizontal_alignment` property:
        
        * Defines top, bottom and left page margins if the value is :attr:`HtmlFixedPageHorizontalAlignment.LEFT`.
        
        * Defines top, bottom and right page margins if the value is :attr:`HtmlFixedPageHorizontalAlignment.RIGHT`.
        
        * Defines top and bottom page margins if the value is :attr:`HtmlFixedPageHorizontalAlignment.CENTER`."""
        ...
    
    @page_margins.setter
    def page_margins(self, value: float):
        ...
    
    @property
    def resources_folder(self) -> str:
        """Specifies the physical folder where resources (images, fonts, css) are saved when exporting a document to Html format.
        Default is ``None``.
        
        Has effect only if :attr:`HtmlFixedSaveOptions.export_embedded_images` property is ``False``.
        
        When you save a :class:`aspose.words.Document` in Html format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`HtmlFixedSaveOptions.resources_folder`
        allows you to specify where the images will be saved and :attr:`HtmlFixedSaveOptions.resources_folder_alias`
        allows to specify how the image URIs will be constructed.
        
        If you save a document into a file and provide a file name, Aspose.Words, by default, saves the
        images in the same folder where the document file is saved. Use :attr:`HtmlFixedSaveOptions.resources_folder`
        to override this behavior.
        
        If you save a document into a stream, Aspose.Words does not have a folder where to save the images,
        but still needs to save the images somewhere. In this case, you need to specify an accessible folder
        by using the :attr:`HtmlFixedSaveOptions.resources_folder` property"""
        ...
    
    @resources_folder.setter
    def resources_folder(self, value: str):
        ...
    
    @property
    def resources_folder_alias(self) -> str:
        """Specifies the name of the folder used to construct image URIs written into an Html document.
        Default is ``None``.
        
        When you save a :class:`aspose.words.Document` in Html format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`HtmlFixedSaveOptions.resources_folder`
        allows you to specify where the images will be saved and :attr:`HtmlFixedSaveOptions.resources_folder_alias`
        allows to specify how the image URIs will be constructed."""
        ...
    
    @resources_folder_alias.setter
    def resources_folder_alias(self, value: str):
        ...
    
    @property
    def export_embedded_images(self) -> bool:
        """Specifies whether images should be embedded into Html document in Base64 format.
        Note setting this flag can significantly increase size of output Html file."""
        ...
    
    @export_embedded_images.setter
    def export_embedded_images(self, value: bool):
        ...
    
    @property
    def export_embedded_fonts(self) -> bool:
        """Specifies whether fonts should be embedded into Html document in Base64 format.
        Note setting this flag can significantly increase size of output Html file."""
        ...
    
    @export_embedded_fonts.setter
    def export_embedded_fonts(self, value: bool):
        ...
    
    @property
    def export_embedded_css(self) -> bool:
        """Specifies whether the CSS (Cascading Style Sheet) should be embedded into Html document."""
        ...
    
    @export_embedded_css.setter
    def export_embedded_css(self, value: bool):
        ...
    
    @property
    def export_embedded_svg(self) -> bool:
        """Specifies whether SVG resources should be embedded into Html document.
        Default value is ``True``."""
        ...
    
    @export_embedded_svg.setter
    def export_embedded_svg(self, value: bool):
        ...
    
    @property
    def font_format(self) -> aspose.words.saving.ExportFontFormat:
        """Gets or sets :class:`ExportFontFormat` used for font exporting.
        Default value is :attr:`ExportFontFormat.WOFF`."""
        ...
    
    @font_format.setter
    def font_format(self, value: aspose.words.saving.ExportFontFormat):
        ...
    
    @property
    def css_class_names_prefix(self) -> str:
        """Specifies prefix which is added to all class names in style.css file.
        Default value is ``"aw"``."""
        ...
    
    @css_class_names_prefix.setter
    def css_class_names_prefix(self, value: str):
        ...
    
    @property
    def resource_saving_callback(self) -> aspose.words.saving.IResourceSavingCallback:
        """Allows to control how resources (images, fonts and css) are saved when a document is exported to fixed page Html format."""
        ...
    
    @resource_saving_callback.setter
    def resource_saving_callback(self, value: aspose.words.saving.IResourceSavingCallback):
        ...
    
    @property
    def encoding(self) -> str:
        """Specifies the encoding to use when exporting to HTML.
        Default value is ``new UTF8Encoding(true)`` (UTF-8 with BOM)."""
        ...
    
    @encoding.setter
    def encoding(self, value: str):
        ...
    
    @property
    def export_form_fields(self) -> bool:
        """Gets or sets indication of whether form fields are exported as interactive
        items (as 'input' tag) rather than converted to text or graphics."""
        ...
    
    @export_form_fields.setter
    def export_form_fields(self, value: bool):
        ...
    
    @property
    def use_target_machine_fonts(self) -> bool:
        """Flag indicates whether fonts from target machine must be used to display the document.
        If this flag is set to ``True``, :attr:`HtmlFixedSaveOptions.font_format` and :attr:`HtmlFixedSaveOptions.export_embedded_fonts` properties do not have effect,
        also :attr:`HtmlFixedSaveOptions.resource_saving_callback` is not fired for fonts.
        Default is ``False``."""
        ...
    
    @use_target_machine_fonts.setter
    def use_target_machine_fonts(self, value: bool):
        ...
    
    @property
    def save_font_face_css_separately(self) -> bool:
        """Flag indicates whether "@font-face" CSS rules should be placed into a separate file "fontFaces.css"
        when a document is being saved with external stylesheet (that is, when :attr:`HtmlFixedSaveOptions.export_embedded_css`
        is ``False``).
        Default value is ``False``, all CSS rules are written into single file "styles.css".
        
        Setting this property to ``True`` restores the old behavior (separate files) for compatibility with legacy code."""
        ...
    
    @save_font_face_css_separately.setter
    def save_font_face_css_separately(self, value: bool):
        ...
    
    ...

class HtmlSaveOptions(aspose.words.saving.SaveOptions):
    """Can be used to specify additional options when saving a document into the
    :attr:`aspose.words.SaveFormat.HTML`, :attr:`aspose.words.SaveFormat.MHTML`, :attr:`aspose.words.SaveFormat.EPUB`,
    :attr:`aspose.words.SaveFormat.AZW3` or :attr:`aspose.words.SaveFormat.MOBI` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of this class that can be used to save a document
        in the :attr:`aspose.words.SaveFormat.HTML` format."""
        ...
    
    @overload
    def __init__(self, save_format: aspose.words.SaveFormat):
        """Initializes a new instance of this class that can be used to save a document
        in the :attr:`aspose.words.SaveFormat.HTML`, :attr:`aspose.words.SaveFormat.MHTML`, :attr:`aspose.words.SaveFormat.EPUB`,
        :attr:`aspose.words.SaveFormat.AZW3` or :attr:`aspose.words.SaveFormat.MOBI` format.
        
        :param save_format: Can be :attr:`aspose.words.SaveFormat.HTML`, :attr:`aspose.words.SaveFormat.MHTML`, :attr:`aspose.words.SaveFormat.EPUB`,
                            :attr:`aspose.words.SaveFormat.AZW3` or :attr:`aspose.words.SaveFormat.MOBI`."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can be :attr:`aspose.words.SaveFormat.HTML`, :attr:`aspose.words.SaveFormat.MHTML`, :attr:`aspose.words.SaveFormat.EPUB`,
        :attr:`aspose.words.SaveFormat.AZW3` or :attr:`aspose.words.SaveFormat.MOBI`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def allow_negative_indent(self) -> bool:
        """Specifies whether negative left and right indents of paragraphs are normalized
        when saving to HTML, MHTML or EPUB. Default value is ``False``.
        
        When negative indent is not allowed, it is exported as zero margin to HTML.
        When negative indent is allowed, a paragraph might appear partially outside of the
        browser window."""
        ...
    
    @allow_negative_indent.setter
    def allow_negative_indent(self, value: bool):
        ...
    
    @property
    def css_style_sheet_file_name(self) -> str:
        """Specifies the path and the name of the Cascading Style Sheet (CSS) file written when a document
        is exported to HTML.
        Default is an empty string.
        
        This property has effect only when saving a document to HTML format
        and external CSS style sheet is requested using :attr:`HtmlSaveOptions.css_style_sheet_type`.
        
        If this property is empty, the CSS file will be saved into the same folder and with the same name as the HTML
        document but with the ".css" extension.
        
        If only path but no file name is specified in this property, the CSS file will be saved into the specified
        folder and will have the same name as the HTML document but with the ".css" extension.
        
        If the folder specified by this property doesn't exist, it will be created automatically before the CSS file
        is saved.
        
        Another way to specify a folder where external CSS file is saved is to use :attr:`HtmlSaveOptions.resource_folder`."""
        ...
    
    @css_style_sheet_file_name.setter
    def css_style_sheet_file_name(self, value: str):
        ...
    
    @property
    def css_style_sheet_type(self) -> aspose.words.saving.CssStyleSheetType:
        """Specifies how CSS (Cascading Style Sheet) styles are exported to HTML, MHTML or EPUB.
        Default value is :attr:`CssStyleSheetType.INLINE` for HTML/MHTML and
        :attr:`CssStyleSheetType.EXTERNAL` for EPUB.
        
        Saving CSS style sheet into an external file is only supported when saving to HTML.
        When you are exporting to one of the container formats (EPUB or MHTML) and specifying
        :attr:`CssStyleSheetType.EXTERNAL`, CSS file will be encapsulated
        into the output package."""
        ...
    
    @css_style_sheet_type.setter
    def css_style_sheet_type(self, value: aspose.words.saving.CssStyleSheetType):
        ...
    
    @property
    def css_class_name_prefix(self) -> str:
        """Specifies a prefix which is added to all CSS class names.
        Default value is an empty string and generated CSS class names have no common prefix.
        
        If this value is not empty, all CSS classes generated by Aspose.Words will start with the specified prefix.
        This might be useful, for example, if you add custom CSS to generated documents and want to prevent class
        name conflicts.
        
        If the value is not ``None`` or empty, it must be a valid CSS identifier.
        
        :raises RuntimeError (Proxy error(ArgumentException)): The value is not empty and is not a valid CSS identifier."""
        ...
    
    @css_class_name_prefix.setter
    def css_class_name_prefix(self, value: str):
        ...
    
    @property
    def document_part_saving_callback(self) -> aspose.words.saving.IDocumentPartSavingCallback:
        """Allows to control how document parts are saved when a document is saved to HTML or EPUB."""
        ...
    
    @document_part_saving_callback.setter
    def document_part_saving_callback(self, value: aspose.words.saving.IDocumentPartSavingCallback):
        ...
    
    @property
    def css_saving_callback(self) -> aspose.words.saving.ICssSavingCallback:
        """Allows to control how CSS styles are saved when a document is saved to HTML, MHTML or EPUB."""
        ...
    
    @css_saving_callback.setter
    def css_saving_callback(self, value: aspose.words.saving.ICssSavingCallback):
        ...
    
    @property
    def document_split_criteria(self) -> aspose.words.saving.DocumentSplitCriteria:
        """Specifies how the document should be split when saving to :attr:`aspose.words.SaveFormat.HTML`,
        :attr:`aspose.words.SaveFormat.EPUB` or :attr:`aspose.words.SaveFormat.AZW3` format.
        Default is :attr:`DocumentSplitCriteria.NONE` for HTML and
        :attr:`DocumentSplitCriteria.HEADING_PARAGRAPH` for EPUB and AZW3.
        
        Normally you would want a document saved to HTML as a single file.
        But in some cases it is preferable to split the output into several smaller HTML pages.
        When saving to HTML format these pages will be output to individual files or streams.
        When saving to EPUB format they will be incorporated into corresponding packages.
        
        A document cannot be split when saving in the MHTML format."""
        ...
    
    @document_split_criteria.setter
    def document_split_criteria(self, value: aspose.words.saving.DocumentSplitCriteria):
        ...
    
    @property
    def document_split_heading_level(self) -> int:
        """Specifies the maximum level of headings at which to split the document.
        Default value is ``2``.
        
        When :attr:`HtmlSaveOptions.document_split_criteria` includes :attr:`DocumentSplitCriteria.HEADING_PARAGRAPH`
        and this property is set to a value from 1 to 9, the document will be split at paragraphs formatted using
        **Heading 1**, **Heading 2** , **Heading 3** etc. styles up to the specified heading level.
        
        By default, only **Heading 1** and **Heading 2** paragraphs cause the document to be split.
        Setting this property to zero will cause the document not to be split at heading paragraphs at all."""
        ...
    
    @document_split_heading_level.setter
    def document_split_heading_level(self, value: int):
        ...
    
    @property
    def encoding(self) -> str:
        """Specifies the encoding to use when exporting to HTML, MHTML or EPUB.
        Default value is ``new UTF8Encoding(false)`` (UTF-8 without BOM)."""
        ...
    
    @encoding.setter
    def encoding(self, value: str):
        ...
    
    @property
    def navigation_map_level(self) -> int:
        """Specifies the maximum level of headings populated to the navigation map when exporting to EPUB, MOBI, or AZW3
        formats. Default value is ``3``.
        
        The navigation map allows user agents to provide an easy way of navigation through the document structure.
        Usually navigation points correspond to headings in the document. In order to populate headings up to level **N**
        assign this value to :attr:`HtmlSaveOptions.navigation_map_level`.
        
        By default, three levels of headings are populated: paragraphs of styles **Heading 1**, **Heading 2**
        and **Heading 3**.
        You can set this property to a value from 1 to 9 in order to request the corresponding maximum level.
        Setting it to zero will reduce the navigation map to only the document root or roots of document parts."""
        ...
    
    @navigation_map_level.setter
    def navigation_map_level(self, value: int):
        ...
    
    @property
    def export_document_properties(self) -> bool:
        """Specifies whether to export built-in and custom document properties to HTML, MHTML or EPUB.
        Default value is ``False``."""
        ...
    
    @export_document_properties.setter
    def export_document_properties(self, value: bool):
        ...
    
    @property
    def export_font_resources(self) -> bool:
        """Specifies whether font resources should be exported to HTML, MHTML or EPUB.
        Default is ``False``.
        
        Exporting font resources allows for consistent document rendering independent of the fonts available
        in a given user's environment.
        
        If :attr:`HtmlSaveOptions.export_font_resources` is set to ``True``, main HTML document will refer to every font via
        the CSS 3 **@font-face** at-rule and fonts will be output as separate files. When exporting to IDPF EPUB or MHTML
        formats, fonts will be embedded into the corresponding package along with other subsidiary files.
        
        If :attr:`HtmlSaveOptions.export_fonts_as_base64` is set to ``True``, fonts will not be saved to separate files.
        Instead, they will be embedded into **@font-face** at-rules in Base64 encoding.
        
        **Important!** When exporting font resources, font licensing issues should be considered. Authors who want to use specific fonts via a downloadable
        font mechanism must always carefully verify that their intended use is within the scope of the font license. Many commercial fonts presently do not
        allow web downloading of their fonts in any form. License agreements that cover some fonts specifically note that usage via **@font-face** rules
        in CSS style sheets is not allowed. Font subsetting can also violate license terms."""
        ...
    
    @export_font_resources.setter
    def export_font_resources(self, value: bool):
        ...
    
    @property
    def export_fonts_as_base64(self) -> bool:
        """Specifies whether fonts resources should be embedded to HTML in Base64 encoding.
        Default is ``False``.
        
        By default, fonts are written to separate files. If this option is set to ``True``, fonts will be embedded
        into the document's CSS in Base64 encoding."""
        ...
    
    @export_fonts_as_base64.setter
    def export_fonts_as_base64(self, value: bool):
        ...
    
    @property
    def export_headers_footers_mode(self) -> aspose.words.saving.ExportHeadersFootersMode:
        """Specifies how headers and footers are output to HTML, MHTML or EPUB.
        Default value is :attr:`ExportHeadersFootersMode.PER_SECTION` for HTML/MHTML
        and :attr:`ExportHeadersFootersMode.NONE` for EPUB.
        
        It is hard to meaningfully output headers and footers to HTML because HTML is not paginated.
        
        When this property is :attr:`ExportHeadersFootersMode.PER_SECTION`, Aspose.Words exports
        only primary headers and footers at the beginning and the end of each section.
        
        When it is :attr:`ExportHeadersFootersMode.FIRST_SECTION_HEADER_LAST_SECTION_FOOTER`
        only first primary header and the last primary footer (including linked to previous) are exported.
        
        You can disable export of headers and footers altogether by setting this property
        to :attr:`ExportHeadersFootersMode.NONE`."""
        ...
    
    @export_headers_footers_mode.setter
    def export_headers_footers_mode(self, value: aspose.words.saving.ExportHeadersFootersMode):
        ...
    
    @property
    def export_images_as_base64(self) -> bool:
        """Specifies whether images are saved in Base64 format to the output HTML, MHTML or EPUB.
        Default is ``False``.
        
        When this property is set to ``True`` images data are exported
        directly into the **img** elements and separate files are not created."""
        ...
    
    @export_images_as_base64.setter
    def export_images_as_base64(self, value: bool):
        ...
    
    @property
    def export_language_information(self) -> bool:
        """Specifies whether language information is exported to HTML, MHTML or EPUB.
        Default is ``False``.
        
        When this property is set to ``True`` Aspose.Words outputs **lang** HTML attribute on the document
        elements that specify language. This can be needed to preserve language related semantics."""
        ...
    
    @export_language_information.setter
    def export_language_information(self, value: bool):
        ...
    
    @property
    def export_list_labels(self) -> aspose.words.saving.ExportListLabels:
        """Controls how list labels are output to HTML, MHTML or EPUB.
        Default value is :attr:`ExportListLabels.AUTO`."""
        ...
    
    @export_list_labels.setter
    def export_list_labels(self, value: aspose.words.saving.ExportListLabels):
        ...
    
    @property
    def metafile_format(self) -> aspose.words.saving.HtmlMetafileFormat:
        """Specifies in what format metafiles are saved when exporting to HTML, MHTML, or EPUB.
        Default value is :attr:`HtmlMetafileFormat.PNG`, meaning that metafiles are rendered to raster PNG images.
        
        Metafiles are not natively displayed by HTML browsers. By default, Aspose.Words converts WMF and EMF
        images into PNG files when exporting to HTML. Other options are to convert metafiles to SVG images or to export
        them as is without conversion.
        
        Some image transforms, in particular image cropping, will not be applied to metafile images if they
        are exported to HTML without conversion."""
        ...
    
    @metafile_format.setter
    def metafile_format(self, value: aspose.words.saving.HtmlMetafileFormat):
        ...
    
    @property
    def export_page_setup(self) -> bool:
        """Specifies whether page setup is exported to HTML, MHTML or EPUB.
        Default is ``False``.
        
        Each :class:`aspose.words.Section` in Aspose.Words document model provides page setup information
        via :class:`aspose.words.PageSetup` class. When you export a document to HTML format you might need to keep this information
        for further usage. In particular, page setup might be important for rendering to paged media (printing)
        or subsequent conversion to the native Microsoft Word file formats (DOCX, DOC, RTF, WML).
        
        In most cases HTML is intended for viewing in browsers where pagination is not performed. So this feature
        is inactive by default."""
        ...
    
    @export_page_setup.setter
    def export_page_setup(self, value: bool):
        ...
    
    @property
    def export_page_margins(self) -> bool:
        """Specifies whether page margins is exported to HTML, MHTML or EPUB.
        Default is ``False``.
        
        Aspose.Words does not show area of page margins by default.
        If any elements are completely or partially clipped by the document edge the displayed area can be extended with
        this option."""
        ...
    
    @export_page_margins.setter
    def export_page_margins(self, value: bool):
        ...
    
    @property
    def export_relative_font_size(self) -> bool:
        """Specifies whether font sizes should be output in relative units when saving to HTML, MHTML or EPUB.
        Default is ``False``.
        
        In many existing documents (HTML, IDPF EPUB) font sizes are specified in relative units. This allows
        applications to adjust text size when viewing/processing documents. For instance, Microsoft Internet Explorer
        has "View-\>Text Size" submenu, Adobe Digital Editions has two buttons: Increase/Decrease Text Size.
        If you expect this functionality to work then set :attr:`HtmlSaveOptions.export_relative_font_size` property to ``True``.
        
        Aspose Words document model contains and operates only with absolute font size units. Relative units need
        additional logic to be recalculated from some initial (standard) size. Font size of **Normal** document style
        is taken as standard. For instance, if **Normal** has 12pt font and some text is 18pt then it will be output
        as **1.5em.** to the HTML.
        
        When this option is enabled, document elements other than text will still have absolute sizes. Also some
        text-related attributes might be expressed absolutely. In particular, line spacing specified with "exactly" rule
        might produce unwanted results when scaling text. So the source documents should be properly designed and tested
        when exporting with :attr:`HtmlSaveOptions.export_relative_font_size` set to ``True``."""
        ...
    
    @export_relative_font_size.setter
    def export_relative_font_size(self, value: bool):
        ...
    
    @property
    def export_text_input_form_field_as_text(self) -> bool:
        """Controls how text input form fields are saved to HTML or MHTML.
        Default value is ``False``.
        
        When set to ``True``, exports text input form fields as normal text.
        When ``False``, exports Word text input form fields as INPUT elements in HTML.
        
        When exporting to EPUB, text input form fields are always saved as text due
        to requirements of this format."""
        ...
    
    @export_text_input_form_field_as_text.setter
    def export_text_input_form_field_as_text(self, value: bool):
        ...
    
    @property
    def export_shapes_as_svg(self) -> bool:
        """Controls whether :class:`aspose.words.drawing.Shape` nodes are converted to SVG images when saving
        to HTML, MHTML, EPUB or AZW3.
        Default value is ``False``.
        
        If this option is set to ``True``, :class:`aspose.words.drawing.Shape` nodes are exported as \<svg\> elements.
        Otherwise, they are rendered to bitmaps and are exported as \<img\> elements."""
        ...
    
    @export_shapes_as_svg.setter
    def export_shapes_as_svg(self, value: bool):
        ...
    
    @property
    def export_drop_down_form_field_as_text(self) -> bool:
        """Controls how drop-down form fields are saved to HTML or MHTML.
        Default value is ``False``.
        
        When set to ``True``, exports drop-down form fields as normal text.
        When ``False``, exports drop-down form fields as SELECT element in HTML.
        
        When exporting to EPUB, text drop-down form fields are always saved as text due
        to requirements of this format."""
        ...
    
    @export_drop_down_form_field_as_text.setter
    def export_drop_down_form_field_as_text(self, value: bool):
        ...
    
    @property
    def export_toc_page_numbers(self) -> bool:
        """Specifies whether to write page numbers to table of contents when saving HTML, MHTML and EPUB.
        Default value is ``False``."""
        ...
    
    @export_toc_page_numbers.setter
    def export_toc_page_numbers(self, value: bool):
        ...
    
    @property
    def export_xhtml_transitional(self) -> bool:
        """Specifies whether to write the DOCTYPE declaration when saving to HTML or MHTML.
        When ``True``, writes a DOCTYPE declaration in the document prior to the root element.
        Default value is ``False``.
        When saving to EPUB or HTML5 (:attr:`HtmlVersion.HTML5`) the DOCTYPE
        declaration is always written.
        
        Aspose.Words always writes well formed HTML regardless of this setting.
        
        When ``True``, the beginning of the HTML output document will look like this:
        
        <?xml version="1.0" encoding="utf-8" standalone="no" ?>
        
        <!DOCTYPE html
        
              PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
        
        Aspose.Words aims to output XHTML according to the XHTML 1.0 Transitional specification,
        but the output will not always validate against the DTD. Some structures inside a Microsoft Word
        document are hard or impossible to map to a document that will validate against the XHTML schema.
        For example, XHTML does not allow nested lists (UL cannot be nested inside another UL element),
        but in Microsoft Word document multilevel lists occur quite often."""
        ...
    
    @export_xhtml_transitional.setter
    def export_xhtml_transitional(self, value: bool):
        ...
    
    @property
    def html_version(self) -> aspose.words.saving.HtmlVersion:
        """Specifies version of HTML standard that should be used when saving the document to HTML or MHTML.
        Default value is :attr:`HtmlVersion.XHTML`."""
        ...
    
    @html_version.setter
    def html_version(self, value: aspose.words.saving.HtmlVersion):
        ...
    
    @property
    def export_roundtrip_information(self) -> bool:
        """Specifies whether to write the roundtrip information when saving to HTML, MHTML or EPUB.
        Default value is ``True`` for HTML and ``False`` for MHTML and EPUB.
        
        Saving of the roundtrip information allows to restore document properties such as tab stops,
        comments, headers and footers during the HTML documents loading back into a :class:`aspose.words.Document` object.
        
        When ``True``, the roundtrip information is exported as -aw-\* CSS properties
        of the corresponding HTML elements.
        
        When ``False``, causes no roundtrip information to be output into produced files."""
        ...
    
    @export_roundtrip_information.setter
    def export_roundtrip_information(self, value: bool):
        ...
    
    @property
    def resource_folder(self) -> str:
        """Specifies a physical folder where all resources like images, fonts, and external CSS are saved when a document
        is exported to HTML. Default is an empty string.
        
        :attr:`HtmlSaveOptions.resource_folder` is the simplest way to specify a folder where all resources should be written.
        Another way is to use individual properties :attr:`HtmlSaveOptions.fonts_folder`, :attr:`HtmlSaveOptions.images_folder`,
        and :attr:`HtmlSaveOptions.css_style_sheet_file_name`.
        
        :attr:`HtmlSaveOptions.resource_folder` has a lower priority than folders specified via :attr:`HtmlSaveOptions.fonts_folder`,
        :attr:`HtmlSaveOptions.images_folder`, and :attr:`HtmlSaveOptions.css_style_sheet_file_name`. For example, if both
        :attr:`HtmlSaveOptions.resource_folder` and :attr:`HtmlSaveOptions.fonts_folder` are specified, fonts will be saved
        to :attr:`HtmlSaveOptions.fonts_folder`, while images and CSS will be saved to :attr:`HtmlSaveOptions.resource_folder`.
        
        If the folder specified by :attr:`HtmlSaveOptions.resource_folder` doesn't exist, it will be created automatically."""
        ...
    
    @resource_folder.setter
    def resource_folder(self, value: str):
        ...
    
    @property
    def resource_folder_alias(self) -> str:
        """Specifies the name of the folder used to construct URIs of all resources written into an HTML document.
        Default is an empty string.
        
        :attr:`HtmlSaveOptions.resource_folder_alias` is the simplest way to specify how URIs for all resource files should be
        constructed. Same information can be specified for images and fonts separately via :attr:`HtmlSaveOptions.images_folder_alias`
        and :attr:`HtmlSaveOptions.fonts_folder_alias` properties, respectively. However, there is no individual property for CSS.
        
        :attr:`HtmlSaveOptions.resource_folder_alias` has lower priority than :attr:`HtmlSaveOptions.fonts_folder_alias`
        and :attr:`HtmlSaveOptions.images_folder_alias`. For example, if both :attr:`HtmlSaveOptions.resource_folder_alias`
        and :attr:`HtmlSaveOptions.fonts_folder_alias` are specified, fonts' URIs will be constructed using
        :attr:`HtmlSaveOptions.fonts_folder_alias`, while URIs of images and CSS will be constructed using
        :attr:`HtmlSaveOptions.resource_folder_alias`.
        
        If :attr:`HtmlSaveOptions.resource_folder_alias` is empty, the :attr:`HtmlSaveOptions.resource_folder` property value will be used
        to construct resource URIs.
        
        If :attr:`HtmlSaveOptions.resource_folder_alias` is set to '.' (dot), resource URIs will contain file names only, without
        any path."""
        ...
    
    @resource_folder_alias.setter
    def resource_folder_alias(self, value: str):
        ...
    
    @property
    def fonts_folder(self) -> str:
        """Specifies the physical folder where fonts are saved when exporting a document to HTML.
        Default is an empty string.
        
        When you save a :class:`aspose.words.Document` in HTML format and :attr:`HtmlSaveOptions.export_font_resources`
        is set to ``True``, Aspose.Words needs to save fonts used in the document as standalone files.
        :attr:`HtmlSaveOptions.fonts_folder` allows you to specify where the fonts will be saved and
        :attr:`HtmlSaveOptions.fonts_folder_alias` allows to specify how the font URIs will be constructed.
        
        If you save a document into a file and provide a file name, Aspose.Words, by default, saves the
        fonts in the same folder where the document file is saved. Use :attr:`HtmlSaveOptions.fonts_folder`
        to override this behavior.
        
        If you save a document into a stream, Aspose.Words does not have a folder where to save the fonts,
        but still needs to save the fonts somewhere. In this case, you need to specify an accessible folder
        in the :attr:`HtmlSaveOptions.fonts_folder` property or provide custom streams via
        the :attr:`HtmlSaveOptions.font_saving_callback` event handler.
        
        If the folder specified by :attr:`HtmlSaveOptions.fonts_folder` doesn't exist, it will be created automatically.
        
        :attr:`HtmlSaveOptions.resource_folder` is another way to specify a folder where fonts should be saved."""
        ...
    
    @fonts_folder.setter
    def fonts_folder(self, value: str):
        ...
    
    @property
    def fonts_folder_alias(self) -> str:
        """Specifies the name of the folder used to construct font URIs written into an HTML document.
        Default is an empty string.
        
        When you save a :class:`aspose.words.Document` in HTML format and :attr:`HtmlSaveOptions.export_font_resources`
        is set to ``True``, Aspose.Words needs to save fonts used in the document as standalone files.
        :attr:`HtmlSaveOptions.fonts_folder` allows you to specify where the fonts will be saved and
        :attr:`HtmlSaveOptions.fonts_folder_alias` allows to specify how the font URIs will be constructed.
        
        If :attr:`HtmlSaveOptions.fonts_folder_alias` is not an empty string, then the font URI written
        to HTML will be *FontsFolderAlias + \<font file name\>*.
        
        If :attr:`HtmlSaveOptions.fonts_folder_alias` is an empty string, then the font URI written
        to HTML will be *FontsFolder + \<font file name\>*.
        
        If :attr:`HtmlSaveOptions.fonts_folder_alias` is set to '.' (dot), then the font file name
        will be written to HTML without path regardless of other options.
        
        Alternative way to specify the name of the folder to construct font URIs
        is to use :attr:`HtmlSaveOptions.resource_folder_alias`."""
        ...
    
    @fonts_folder_alias.setter
    def fonts_folder_alias(self, value: str):
        ...
    
    @property
    def font_resources_subsetting_size_threshold(self) -> int:
        """Controls which font resources need subsetting when saving to HTML, MHTML or EPUB.
        Default is ``0``.
        
        :attr:`HtmlSaveOptions.export_font_resources` allows exporting fonts as subsidiary files or as parts of the output
        package. If the document uses many fonts, especially with large number of glyphs, then output size can grow
        significantly. Font subsetting reduces the size of the exported font resource by filtering out glyphs that
        are not used by the current document.
        
        Font subsetting works as follows:
        
        * By default, all exported fonts are subsetted.
        
        * Setting :attr:`HtmlSaveOptions.font_resources_subsetting_size_threshold` to a positive value
          instructs Aspose.Words to subset fonts which file size is larger than the specified value.
        
        * Setting the property to int.MaxValue C# constant
          suppresses font subsetting.
        
        **Important!** When exporting font resources, font licensing issues should be considered. Authors who want to use specific fonts via a downloadable
        font mechanism must always carefully verify that their intended use is within the scope of the font license. Many commercial fonts presently do not
        allow web downloading of their fonts in any form. License agreements that cover some fonts specifically note that usage via **@font-face** rules
        in CSS style sheets is not allowed. Font subsetting can also violate license terms."""
        ...
    
    @font_resources_subsetting_size_threshold.setter
    def font_resources_subsetting_size_threshold(self, value: int):
        ...
    
    @property
    def font_saving_callback(self) -> aspose.words.saving.IFontSavingCallback:
        """Allows to control how fonts are saved when a document is saved to HTML, MHTML or EPUB."""
        ...
    
    @font_saving_callback.setter
    def font_saving_callback(self, value: aspose.words.saving.IFontSavingCallback):
        ...
    
    @property
    def images_folder(self) -> str:
        """Specifies the physical folder where images are saved when exporting a document to HTML format.
        Default is an empty string.
        
        When you save a :class:`aspose.words.Document` in HTML format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`HtmlSaveOptions.images_folder`
        allows you to specify where the images will be saved and :attr:`HtmlSaveOptions.images_folder_alias`
        allows to specify how the image URIs will be constructed.
        
        If you save a document into a file and provide a file name, Aspose.Words, by default, saves the
        images in the same folder where the document file is saved. Use :attr:`HtmlSaveOptions.images_folder`
        to override this behavior.
        
        If you save a document into a stream, Aspose.Words does not have a folder where to save the images,
        but still needs to save the images somewhere. In this case, you need to specify an accessible folder
        in the :attr:`HtmlSaveOptions.images_folder` property or provide custom streams via
        the :attr:`HtmlSaveOptions.image_saving_callback` event handler.
        
        If the folder specified by :attr:`HtmlSaveOptions.images_folder` doesn't exist, it will be created automatically.
        
        :attr:`HtmlSaveOptions.resource_folder` is another way to specify a folder where images should be saved."""
        ...
    
    @images_folder.setter
    def images_folder(self, value: str):
        ...
    
    @property
    def images_folder_alias(self) -> str:
        """Specifies the name of the folder used to construct image URIs written into an HTML document.
        Default is an empty string.
        
        When you save a :class:`aspose.words.Document` in HTML format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`HtmlSaveOptions.images_folder`
        allows you to specify where the images will be saved and :attr:`HtmlSaveOptions.images_folder_alias`
        allows to specify how the image URIs will be constructed.
        
        If :attr:`HtmlSaveOptions.images_folder_alias` is not an empty string, then the image URI written
        to HTML will be *ImagesFolderAlias + \<image file name\>*.
        
        If :attr:`HtmlSaveOptions.images_folder_alias` is an empty string, then the image URI written
        to HTML will be *ImagesFolder + \<image file name\>*.
        
        If :attr:`HtmlSaveOptions.images_folder_alias` is set to '.' (dot), then the image file name
        will be written to HTML without path regardless of other options.
        
        Alternative way to specify the name of the folder to construct image URIs
        is to use :attr:`HtmlSaveOptions.resource_folder_alias`."""
        ...
    
    @images_folder_alias.setter
    def images_folder_alias(self, value: str):
        ...
    
    @property
    def image_resolution(self) -> int:
        """Specifies the output resolution for images when exporting to HTML, MHTML or EPUB.
        Default is ``96 dpi``.
        
        This property effects raster images when :attr:`HtmlSaveOptions.scale_image_to_shape_size`
        is ``True`` and effects metafiles exported as raster images. Some image properties such as cropping
        or rotation require saving transformed images and in this case transformed images are created in the given
        resolution."""
        ...
    
    @image_resolution.setter
    def image_resolution(self, value: int):
        ...
    
    @property
    def image_saving_callback(self) -> aspose.words.saving.IImageSavingCallback:
        """Allows to control how images are saved when a document is saved to HTML, MHTML or EPUB."""
        ...
    
    @image_saving_callback.setter
    def image_saving_callback(self, value: aspose.words.saving.IImageSavingCallback):
        ...
    
    @property
    def scale_image_to_shape_size(self) -> bool:
        """Specifies whether images are scaled by Aspose.Words to the bounding shape size when exporting to HTML, MHTML
        or EPUB.
        Default value is ``True``.
        
        An image in a Microsoft Word document is a shape. The shape has a size and the image
        has its own size. The sizes are not directly linked. For example, the image can be 1024x786 pixels,
        but shape that displays this image can be 400x300 points.
        
        In order to display an image in the browser, it must be scaled to the shape size.
        The :attr:`HtmlSaveOptions.scale_image_to_shape_size` property controls where the scaling of the image
        takes place: in Aspose.Words during export to HTML or in the browser when displaying the document.
        
        When :attr:`HtmlSaveOptions.scale_image_to_shape_size` is ``True``, the image is scaled by Aspose.Words
        using high quality scaling during export to HTML. When :attr:`HtmlSaveOptions.scale_image_to_shape_size`
        is ``False``, the image is output with its original size and the browser has to scale it.
        
        In general, browsers do quick and poor quality scaling. As a result, you will normally get better
        display quality in the browser and smaller file size when :attr:`HtmlSaveOptions.scale_image_to_shape_size` is ``True``,
        but better printing quality and faster conversion when :attr:`HtmlSaveOptions.scale_image_to_shape_size` is ``False``.
        
        In addition to shapes containing individual raster images, this option also affects group shapes consisting
        of raster images. If :attr:`HtmlSaveOptions.scale_image_to_shape_size` is ``False`` and a group shape contains raster images
        whose intrinsic resolution is higher than the value specified in :attr:`HtmlSaveOptions.image_resolution`, Aspose.Words will
        increase rendering resolution for that group. This allows to better preserve quality of grouped high resolution
        images when saving to HTML."""
        ...
    
    @scale_image_to_shape_size.setter
    def scale_image_to_shape_size(self, value: bool):
        ...
    
    @property
    def table_width_output_mode(self) -> aspose.words.saving.HtmlElementSizeOutputMode:
        """Controls how table, row and cell widths are exported to HTML, MHTML or EPUB.
        Default value is :attr:`HtmlElementSizeOutputMode.ALL`.
        
        In the HTML format, table, row and cell elements
        (**\<table\>**, **\<tr\>**, **\<th\>**, **\<td\>**)
        can have their widths specified either in relative (percentage) or in absolute units.
        In a document in Aspose.Words, tables, rows and cells can have their widths specified
        using either relative or absolute units too.
        
        When you convert a document to HTML using Aspose.Words, you might want to control how
        table, row and cell widths are exported to affect how the resulting document is displayed
        in the visual agent (e.g. a browser or viewer).
        
        Use this property as a filter to specify what table widths values are exported into the destination document.
        For example, if you are converting a document to EPUB and intend to view the document on a mobile reading device,
        then you probably want to avoid exporting absolute width values. To do this you need to specify
        the output mode :attr:`HtmlElementSizeOutputMode.RELATIVE_ONLY` or :attr:`HtmlElementSizeOutputMode.NONE`
        so the viewer on the mobile device can layout the table to fit the width of the screen as best as it can."""
        ...
    
    @table_width_output_mode.setter
    def table_width_output_mode(self, value: aspose.words.saving.HtmlElementSizeOutputMode):
        ...
    
    @property
    def office_math_output_mode(self) -> aspose.words.saving.HtmlOfficeMathOutputMode:
        """Controls how OfficeMath objects are exported to HTML, MHTML or EPUB.
        Default value is :attr:`HtmlOfficeMathOutputMode.IMAGE`."""
        ...
    
    @office_math_output_mode.setter
    def office_math_output_mode(self, value: aspose.words.saving.HtmlOfficeMathOutputMode):
        ...
    
    @property
    def export_original_url_for_linked_images(self) -> bool:
        """Specifies whether original URL should be used as the URL of the linked images.
        Default value is ``False``.
        
        If value is set to ``True``
        :attr:`aspose.words.drawing.ImageData.source_full_name` value is used
        as the URL of linked images and linked images are not loaded into document's folder
        or :attr:`HtmlSaveOptions.images_folder`.
        
        If value is set to ``False`` linked images are loaded into document's folder
        or :attr:`HtmlSaveOptions.images_folder` and URL of each linked image is constructed depending
        on document's folder, :attr:`HtmlSaveOptions.images_folder`
        and :attr:`HtmlSaveOptions.images_folder_alias` properties."""
        ...
    
    @export_original_url_for_linked_images.setter
    def export_original_url_for_linked_images(self, value: bool):
        ...
    
    @property
    def export_cid_urls_for_mhtml_resources(self) -> bool:
        """Specifies whether to use CID (Content-ID) URLs to reference resources (images, fonts, CSS) included in MHTML
        documents. Default value is ``False``.
        
        This option affects only documents being saved to MHTML.
        
        By default, resources in MHTML documents are referenced by file name (for example, "image.png"), which
        are matched against "Content-Location" headers of MIME parts.
        
        This option enables an alternative method, where references to resource files are written as CID (Content-ID)
        URLs (for example, "cid:image.png") and are matched against "Content-ID" headers.
        
        In theory, there should be no difference between the two referencing methods and either of them should work
        fine in any browser or mail agent. In practice, however, some agents fail to fetch resources by file name. If your
        browser or mail agent refuses to load resources included in an MTHML document (doesn't show images or doesn't load
        CSS styles), try exporting the document with CID URLs."""
        ...
    
    @export_cid_urls_for_mhtml_resources.setter
    def export_cid_urls_for_mhtml_resources(self, value: bool):
        ...
    
    @property
    def resolve_font_names(self) -> bool:
        """Specifies whether font family names used in the document are resolved and substituted according to
        :attr:`aspose.words.Document.font_settings` when being written into HTML-based formats.
        
        By default, this option is set to ``False`` and font family names are written to HTML as specified
        in source documents. That is, :attr:`aspose.words.Document.font_settings` are ignored and no resolution or substitution
        of font family names is performed.
        
        If this option is set to ``True``, Aspose.Words uses :attr:`aspose.words.Document.font_settings` to resolve
        each font family name specified in a source document into the name of an available font family, performing
        font substitution as required."""
        ...
    
    @resolve_font_names.setter
    def resolve_font_names(self, value: bool):
        ...
    
    ...

class ICssSavingCallback:
    """Implement this interface if you want to control how Aspose.Words saves CSS (Cascading Style Sheet) when
    saving a document to HTML."""
    
    def css_saving(self, args: aspose.words.saving.CssSavingArgs) -> None:
        """Called when Aspose.Words saves an CSS (Cascading Style Sheet)."""
        ...
    
    ...

class IDocumentPartSavingCallback:
    """Implement this interface if you want to receive notifications and control how
    Aspose.Words saves document parts when exporting a document to :attr:`aspose.words.SaveFormat.HTML`
    or :attr:`aspose.words.SaveFormat.EPUB` format."""
    
    def document_part_saving(self, args: aspose.words.saving.DocumentPartSavingArgs) -> None:
        """Called when Aspose.Words is about to save a document part."""
        ...
    
    ...

class IDocumentSavingCallback:
    """Implement this interface if you want to have your own custom method called during saving a document."""
    
    def notify(self, args: aspose.words.saving.DocumentSavingArgs) -> None:
        """This is called to notify of document saving progress.
        
        :param args: An argument of the event.
        
        The primary uses for this interface is to allow application code to obtain progress status and abort saving process.
        
        An exception should be threw from the progress callback for abortion and it should be caught in the consumer code."""
        ...
    
    ...

class IFontSavingCallback:
    """Implement this interface if you want to receive notifications and control how
    Aspose.Words saves fonts when exporting a document to HTML format."""
    
    def font_saving(self, args: aspose.words.saving.FontSavingArgs) -> None:
        """Called when Aspose.Words is about to save a font resource."""
        ...
    
    ...

class IImageSavingCallback:
    """Implement this interface if you want to control how Aspose.Words saves images when
    saving a document to HTML. May be used by other formats."""
    
    def image_saving(self, args: aspose.words.saving.ImageSavingArgs) -> None:
        """Called when Aspose.Words saves an image to HTML."""
        ...
    
    ...

class IPageSavingCallback:
    """Implement this interface if you want to control how Aspose.Words saves separate pages when
    saving a document to fixed page formats."""
    
    def page_saving(self, args: aspose.words.saving.PageSavingArgs) -> None:
        """Called when Aspose.Words saves a separate page to fixed page formats."""
        ...
    
    ...

class IResourceSavingCallback:
    """Implement this interface if you want to control how Aspose.Words saves external resources (images, fonts and css) when
    saving a document to fixed page HTML or SVG."""
    
    def resource_saving(self, args: aspose.words.saving.ResourceSavingArgs) -> None:
        """Called when Aspose.Words saves an external resource to fixed page HTML or SVG formats."""
        ...
    
    ...

class ImageSaveOptions(aspose.words.saving.FixedPageSaveOptions):
    """Allows to specify additional options when rendering document pages or shapes to images.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self, save_format: aspose.words.SaveFormat):
        """Initializes a new instance of this class that can be used to save rendered images in the
        :attr:`aspose.words.SaveFormat.TIFF`, :attr:`aspose.words.SaveFormat.PNG`, :attr:`aspose.words.SaveFormat.BMP`,
        :attr:`aspose.words.SaveFormat.JPEG`, :attr:`aspose.words.SaveFormat.EMF`, :attr:`aspose.words.SaveFormat.EPS`,
        :attr:`aspose.words.SaveFormat.WEB_P` or :attr:`aspose.words.SaveFormat.SVG` format.
        
        :param save_format: Can be
                            :attr:`aspose.words.SaveFormat.TIFF`, :attr:`aspose.words.SaveFormat.PNG`, :attr:`aspose.words.SaveFormat.BMP`,
                            :attr:`aspose.words.SaveFormat.JPEG`, :attr:`aspose.words.SaveFormat.EMF`, :attr:`aspose.words.SaveFormat.EPS`
                            :attr:`aspose.words.SaveFormat.WEB_P` or :attr:`aspose.words.SaveFormat.SVG` format."""
        ...
    
    def clone(self) -> aspose.words.saving.ImageSaveOptions:
        """Creates a deep clone of this object."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the rendered document pages or shapes will be saved if this save options object is used.
        Can be a raster
        :attr:`aspose.words.SaveFormat.TIFF`, :attr:`aspose.words.SaveFormat.PNG`, :attr:`aspose.words.SaveFormat.BMP`,
        :attr:`aspose.words.SaveFormat.JPEG` or vector :attr:`aspose.words.SaveFormat.EMF`, :attr:`aspose.words.SaveFormat.EPS`,
        :attr:`aspose.words.SaveFormat.WEB_P`, :attr:`aspose.words.SaveFormat.SVG`.
        
        The number of other options depends on the selected format.
        
        Also, it is possible to save to SVG both via :class:`ImageSaveOptions` and via :class:`SvgSaveOptions`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def page_set(self) -> aspose.words.saving.PageSet:
        """Gets or sets the pages to render.
        Default is all the pages in the document.
        
        This property has effect only when rendering document pages. This property is ignored when rendering shapes to images."""
        ...
    
    @page_set.setter
    def page_set(self, value: aspose.words.saving.PageSet):
        ...
    
    @property
    def metafile_rendering_options(self) -> aspose.words.saving.MetafileRenderingOptions:
        """Allows to specify how metafiles are treated in the rendered output.
        
        When :attr:`MetafileRenderingMode.VECTOR` is specified, Aspose.Words renders
        metafile to vector graphics using its own metafile rendering engine first and then renders vector
        graphics to the image.
        
        When :attr:`MetafileRenderingMode.BITMAP` is specified, Aspose.Words renders
        metafile directly to the image using the GDI+ metafile rendering engine.
        
        GDI+ metafile rendering engine works faster, supports almost all metafile features but on low
        resolutions may produce inconsistent result when compared to the rest of vector graphics (especially for text)
        on the page. Aspose.Words metafile rendering engine will produce more consistent result even
        on low resolutions but works slower and may inaccurately render complex metafiles.
        
        The default value for :class:`MetafileRenderingMode` is :attr:`MetafileRenderingMode.BITMAP`."""
        ...
    
    @property
    def jpeg_quality(self) -> int:
        """Gets or sets a value determining the quality of the generated JPEG images.
        
        Has effect only when saving to JPEG.
        
        Use this property to get or set the quality of generated images when saving in JPEG format.
        The value may vary from 0 to 100 where 0 means worst quality but maximum compression and 100
        means best quality but minimum compression.
        
        The default value is 95."""
        ...
    
    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...
    
    @property
    def paper_color(self) -> aspose.pydrawing.Color:
        """Gets or sets the background (paper) color for the generated images.
        The default value is aspose.pydrawing.Color.white.
        
        When rendering pages of a document that specifies its own background color,
        then the document background color will override the color specified by this property."""
        ...
    
    @paper_color.setter
    def paper_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def pixel_format(self) -> aspose.words.saving.ImagePixelFormat:
        """Gets or sets the pixel format for the generated images.
        
        This property has effect only when saving to raster image formats.
        
        The default value is :attr:`ImagePixelFormat.FORMAT_32BPP_ARGB`.
        
        Pixel format of the output image may differ from the set value
        because of work of GDI+."""
        ...
    
    @pixel_format.setter
    def pixel_format(self, value: aspose.words.saving.ImagePixelFormat):
        ...
    
    @property
    def horizontal_resolution(self) -> float:
        """Gets or sets the horizontal resolution for the generated images, in dots per inch.
        
        This property has effect only when saving to raster image formats and affects the output size in pixels.
        
        The default value is 96."""
        ...
    
    @horizontal_resolution.setter
    def horizontal_resolution(self, value: float):
        ...
    
    @property
    def vertical_resolution(self) -> float:
        """Gets or sets the vertical resolution for the generated images, in dots per inch.
        
        This property has effect only when saving to raster image formats and affects the output size in pixels.
        
        The default value is 96."""
        ...
    
    @vertical_resolution.setter
    def vertical_resolution(self, value: float):
        ...
    
    @property
    def image_size(self) -> aspose.pydrawing.Size:
        """Gets or sets the size of a generated image in pixels.
        
        This property has effect only when saving to raster image formats.
        
        The default value is (0 x 0), which means that the size of the generated image will be calculated
        according to the size of the image in points, the specified resolution and scale."""
        ...
    
    @image_size.setter
    def image_size(self, value: aspose.pydrawing.Size):
        ...
    
    @property
    def tiff_compression(self) -> aspose.words.saving.TiffCompression:
        """Gets or sets the type of compression to apply when saving generated images to the TIFF format.
        
        Has effect only when saving to TIFF.
        
        The default value is :attr:`TiffCompression.LZW`."""
        ...
    
    @tiff_compression.setter
    def tiff_compression(self, value: aspose.words.saving.TiffCompression):
        ...
    
    @property
    def image_color_mode(self) -> aspose.words.saving.ImageColorMode:
        """Gets or sets the color mode for the generated images.
        
        This property has effect only when saving to raster image formats.
        
        The default value is :attr:`ImageColorMode.NONE`."""
        ...
    
    @image_color_mode.setter
    def image_color_mode(self, value: aspose.words.saving.ImageColorMode):
        ...
    
    @property
    def image_brightness(self) -> float:
        """Gets or sets the brightness for the generated images.
        
        This property has effect only when saving to raster image formats.
        
        The default value is 0.5. The value must be in the range between 0 and 1."""
        ...
    
    @image_brightness.setter
    def image_brightness(self, value: float):
        ...
    
    @property
    def image_contrast(self) -> float:
        """Gets or sets the contrast for the generated images.
        
        This property has effect only when saving to raster image formats.
        
        The default value is 0.5. The value must be in the range between 0 and 1."""
        ...
    
    @image_contrast.setter
    def image_contrast(self, value: float):
        ...
    
    @property
    def scale(self) -> float:
        """Gets or sets the zoom factor for the generated images.
        
        The default value is 1.0. The value must be greater than 0."""
        ...
    
    @scale.setter
    def scale(self, value: float):
        ...
    
    @property
    def tiff_binarization_method(self) -> aspose.words.saving.ImageBinarizationMethod:
        """Gets or sets method used while converting images to 1 bpp format
        when :attr:`ImageSaveOptions.save_format` is :attr:`aspose.words.SaveFormat.TIFF` and
        :attr:`ImageSaveOptions.tiff_compression` is equal to :attr:`TiffCompression.CCITT3` or :attr:`TiffCompression.CCITT4`.
        
        The default value is :attr:`ImageBinarizationMethod.THRESHOLD`."""
        ...
    
    @tiff_binarization_method.setter
    def tiff_binarization_method(self, value: aspose.words.saving.ImageBinarizationMethod):
        ...
    
    @property
    def threshold_for_floyd_steinberg_dithering(self) -> int:
        """Gets or sets the threshold that determines the value
        of the binarization error in the Floyd-Steinberg method.
        when :class:`ImageBinarizationMethod` is :attr:`ImageBinarizationMethod.FLOYD_STEINBERG_DITHERING`.
        
        The default value is 128."""
        ...
    
    @threshold_for_floyd_steinberg_dithering.setter
    def threshold_for_floyd_steinberg_dithering(self, value: int):
        ...
    
    @property
    def use_gdi_emf_renderer(self) -> bool:
        """Gets or sets a value determining whether to use GDI+ or Aspose.Words metafile renderer when saving to EMF.
        
        If set to ``True`` GDI+ metafile renderer is used. I.e. content is written to GDI+ graphics
        object and saved to metafile.
        
        If set to ``False`` Aspose.Words metafile renderer is used. I.e. content is written directly
        to the metafile format with Aspose.Words.
        
        Has effect only when saving to EMF.
        
        GDI+ saving works only on .NET.
        
        The default value is ``True``."""
        ...
    
    @use_gdi_emf_renderer.setter
    def use_gdi_emf_renderer(self, value: bool):
        ...
    
    ...

class ImageSavingArgs:
    """Provides data for the :meth:`IImageSavingCallback.image_saving` event.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article.
    
    By default, when Aspose.Words saves a document to HTML, it saves each image into
    a separate file. Aspose.Words uses the document file name and a unique number to generate unique file name
    for each image found in the document.
    
    :class:`ImageSavingArgs` allows to redefine how image file names are generated or to
    completely circumvent saving of images into files by providing your own stream objects.
    
    To apply your own logic for generating image file names use the
    :attr:`ImageSavingArgs.image_file_name`, :attr:`ImageSavingArgs.current_shape` and :attr:`ImageSavingArgs.is_image_available`
    properties.
    
    To save images into streams instead of files, use the :attr:`ImageSavingArgs.image_stream` property."""
    
    @property
    def document(self) -> aspose.words.Document:
        """Gets the document object that is currently being saved."""
        ...
    
    @property
    def current_shape(self) -> aspose.words.drawing.ShapeBase:
        """Gets the :class:`aspose.words.drawing.ShapeBase` object corresponding to the shape or group shape
        that is about to be saved.
        
        :class:`IImageSavingCallback` can be fired while saving either a shape or a group shape.
        That's why the property has :class:`aspose.words.drawing.ShapeBase` type. You can check whether it's a group shape comparing
        :attr:`aspose.words.drawing.ShapeBase.shape_type` with :attr:`aspose.words.drawing.ShapeType.GROUP` or by casting it to one of derived classes:
        :class:`aspose.words.drawing.Shape` or :class:`aspose.words.drawing.GroupShape`.
        
        Aspose.Words uses the document file name and a unique number to generate unique file name
        for each image found in the document. You can use the :attr:`ImageSavingArgs.current_shape` property to generate
        a "better" file name by examining shape properties such as :attr:`aspose.words.drawing.ImageData.title`
        (Shape only), :attr:`aspose.words.drawing.ImageData.source_full_name` (Shape only)
        and :attr:`aspose.words.drawing.ShapeBase.name`. Of course you can build file names using any other properties or criteria
        but note that subsidiary file names must be unique within the export operation.
        
        Some images in the document can be unavailable. To check image availability
        use the :attr:`ImageSavingArgs.is_image_available` property."""
        ...
    
    @property
    def is_image_available(self) -> bool:
        """Returns ``True`` if the current image is available for export.
        
        Some images in the document can be unavailable, for example, because the image
        is linked and the link is inaccessible or does not point to a valid image.
        In this case Aspose.Words exports an icon with a red cross. This property returns
        ``True`` if the original image is available; returns ``False`` if the original
        image is not available and a "no image" icon will be offered for save.
        
        When saving a group shape or a shape that doesn't require any image this property
        is always ``True``."""
        ...
    
    @property
    def image_file_name(self) -> str:
        """Gets or sets the file name (without path) where the image will be saved to.
        
        This property allows you to redefine how the image file names are generated
        during export to HTML.
        
        When the event is fired, this property contains the file name that was generated
        by Aspose.Words. You can change the value of this property to save the image into a
        different file. Note that file names must be unique.
        
        Aspose.Words automatically generates a unique file name for every embedded image when
        exporting to HTML format. How the image file name is generated
        depends on whether you save the document to a file or to a stream.
        
        When saving a document to a file, the generated image file name looks like
        *\<document base file name\>.\<image number\>.\<extension\>*.
        
        When saving a document to a stream, the generated image file name looks like
        *Aspose.Words.\<document guid\>.\<image number\>.\<extension\>*.
        
        :attr:`ImageSavingArgs.image_file_name` must contain only the file name without the path.
        Aspose.Words determines the path for saving and the value of the ``src`` attribute for writing
        to HTML using the document file name, the :attr:`HtmlSaveOptions.images_folder` and
        :attr:`HtmlSaveOptions.images_folder_alias` properties."""
        ...
    
    @image_file_name.setter
    def image_file_name(self, value: str):
        ...
    
    @property
    def keep_image_stream_open(self) -> bool:
        """Specifies whether Aspose.Words should keep the stream open or close it after saving an image.
        
        Default is ``False`` and Aspose.Words will close the stream you provided
        in the :attr:`ImageSavingArgs.image_stream` property after writing an image into it.
        Specify ``True`` to keep the stream open."""
        ...
    
    @keep_image_stream_open.setter
    def keep_image_stream_open(self, value: bool):
        ...
    
    @property
    def image_stream(self) -> io.BytesIO:
        """Allows to specify the stream where the image will be saved to.
        
        This property allows you to save images to streams instead of files during HTML.
        
        The default value is ``None``. When this property is ``None``, the image
        will be saved to a file specified in the :attr:`ImageSavingArgs.image_file_name` property.
        
        Using :class:`IImageSavingCallback` you cannot substitute one image with
        another. It is intended only for control over location where to save images."""
        ...
    
    @image_stream.setter
    def image_stream(self, value: io.BytesIO):
        ...
    
    ...

class MarkdownSaveOptions(aspose.words.saving.TxtSaveOptionsBase):
    """Class to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.MARKDOWN` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        """Initializes a new instance of this class that can be used to save a document
        in the :attr:`aspose.words.SaveFormat.MARKDOWN` format."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.MARKDOWN`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def table_content_alignment(self) -> aspose.words.saving.TableContentAlignment:
        """Gets or sets a value that specifies how to align contents in tables
        when exporting into the :attr:`aspose.words.SaveFormat.MARKDOWN` format.
        The default value is :attr:`TableContentAlignment.AUTO`."""
        ...
    
    @table_content_alignment.setter
    def table_content_alignment(self, value: aspose.words.saving.TableContentAlignment):
        ...
    
    @property
    def images_folder(self) -> str:
        """Specifies the physical folder where images are saved when exporting a document to
        the :attr:`aspose.words.SaveFormat.MARKDOWN` format. Default is an empty string.
        
        When you save a :class:`aspose.words.Document` in :attr:`aspose.words.SaveFormat.MARKDOWN` format,
        Aspose.Words needs to save all images embedded in the document as standalone files.
        :attr:`MarkdownSaveOptions.images_folder` allows you to specify where the images will be saved.
        
        If you save a document into a file and provide a file name, Aspose.Words, by default, saves the images in
        the same folder where the document file is saved. Use :attr:`MarkdownSaveOptions.images_folder` to override this behavior.
        
        If you save a document into a stream, Aspose.Words does not have a folder
        where to save the images, but still needs to save the images somewhere. In this case,
        you need to specify an accessible folder in the :attr:`MarkdownSaveOptions.images_folder` property.
        
        If the folder specified by :attr:`MarkdownSaveOptions.images_folder` doesn't exist, it will be created automatically."""
        ...
    
    @images_folder.setter
    def images_folder(self, value: str):
        ...
    
    @property
    def images_folder_alias(self) -> str:
        """Specifies the name of the folder used to construct image URIs written into a document.
        Default is an empty string.
        
        When you save a :class:`aspose.words.Document` in :attr:`aspose.words.SaveFormat.MARKDOWN` format,
        Aspose.Words needs to save all images embedded in the document as standalone files.
        :attr:`MarkdownSaveOptions.images_folder` allows you to specify where the images will be saved and
        :attr:`MarkdownSaveOptions.images_folder_alias` allows to specify how the image URIs will be constructed.
        
        If :attr:`MarkdownSaveOptions.images_folder_alias` is not an empty string, then the image URI written
        to Markdown will be *ImagesFolderAlias + \<image file name\>*.
        
        If :attr:`MarkdownSaveOptions.images_folder_alias` is an empty string, then the image URI written
        to Markdown will be *ImagesFolder + \<image file name\>*.
        
        If :attr:`MarkdownSaveOptions.images_folder_alias` is set to '.' (dot), then the image file name
        will be written to Markdown without path regardless of other options."""
        ...
    
    @images_folder_alias.setter
    def images_folder_alias(self, value: str):
        ...
    
    @property
    def image_saving_callback(self) -> aspose.words.saving.IImageSavingCallback:
        """Allows to control how images are saved when a document is saved to
        :attr:`aspose.words.SaveFormat.MARKDOWN` format."""
        ...
    
    @image_saving_callback.setter
    def image_saving_callback(self, value: aspose.words.saving.IImageSavingCallback):
        ...
    
    @property
    def export_images_as_base64(self) -> bool:
        """Specifies whether images are saved in Base64 format to the output file.
        Default value is ``False``.
        
        When this property is set to ``True`` images data are exported
        directly into the **img** elements and separate files are not created."""
        ...
    
    @export_images_as_base64.setter
    def export_images_as_base64(self, value: bool):
        ...
    
    @property
    def list_export_mode(self) -> aspose.words.saving.MarkdownListExportMode:
        """Specifies how list items will be written to the output file.
        Default value is :attr:`MarkdownListExportMode.MARKDOWN_SYNTAX`.
        
        When this property is set to :attr:`MarkdownListExportMode.PLAIN_TEXT` all list labels are
        updated using :meth:`aspose.words.Document.update_list_labels` and exported with their actual values. Such lists
        can be non-compatible with Markdown format and will be recognized as plain text upon importing in this case.
        
        When this property is set to :attr:`MarkdownListExportMode.MARKDOWN_SYNTAX`, writer tries to export
        list items in manner that allows to numerate list items in automatic mode by Markdown."""
        ...
    
    @list_export_mode.setter
    def list_export_mode(self, value: aspose.words.saving.MarkdownListExportMode):
        ...
    
    @property
    def export_underline_formatting(self) -> bool:
        """Gets or sets a boolean value indicating either to export underline
        text formatting as sequence of two plus characters "++".
        The default value is ``False``."""
        ...
    
    @export_underline_formatting.setter
    def export_underline_formatting(self, value: bool):
        ...
    
    @property
    def link_export_mode(self) -> aspose.words.saving.MarkdownLinkExportMode:
        """Specifies how links will be written to the output file.
        Default value is :attr:`MarkdownLinkExportMode.AUTO`."""
        ...
    
    @link_export_mode.setter
    def link_export_mode(self, value: aspose.words.saving.MarkdownLinkExportMode):
        ...
    
    ...

class MetafileRenderingOptions:
    """Allows to specify additional metafile rendering options.
    To learn more, visit the `Handling Windows Metafiles <https://docs.aspose.com/words/python-net/handling-windows-metafiles/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def rendering_mode(self) -> aspose.words.saving.MetafileRenderingMode:
        """Gets or sets a value determining how metafile images should be rendered.
        
        The default value depends on the save format. For images it is :attr:`MetafileRenderingMode.BITMAP`.
        For other formats it is :attr:`MetafileRenderingMode.VECTOR_WITH_FALLBACK`."""
        ...
    
    @rendering_mode.setter
    def rendering_mode(self, value: aspose.words.saving.MetafileRenderingMode):
        ...
    
    @property
    def emf_plus_dual_rendering_mode(self) -> aspose.words.saving.EmfPlusDualRenderingMode:
        """Gets or sets a value determining how EMF+ Dual metafiles should be rendered.
        
        EMF+ Dual metafiles contains both EMF+ and EMF parts. MS Word and GDI+ always renders EMF+ part.
        Aspose.Words currently doesn't fully supports all EMF+ records and in some cases rendering result of
        EMF part looks better then rendering result of EMF+ part.
        
        This option is used only when metafile is rendered as vector graphics. When metafile is rendered
        to bitmap, EMF+ part is always used.
        
        The default value is :attr:`EmfPlusDualRenderingMode.EMF_PLUS_WITH_FALLBACK`."""
        ...
    
    @emf_plus_dual_rendering_mode.setter
    def emf_plus_dual_rendering_mode(self, value: aspose.words.saving.EmfPlusDualRenderingMode):
        ...
    
    @property
    def use_emf_embedded_to_wmf(self) -> bool:
        """Gets or sets a value determining how WMF metafiles with embedded EMF metafiles should be rendered.
        
        WMF metafiles could contain embedded EMF data. MS Word in most cases uses embedded EMF data.
        GDI+ always uses WMF data.
        
        When this value is set to ``True``, Aspose.Words uses embedded EMF data when rendering.
        
        When this value is set to ``False``, Aspose.Words uses WMF data when rendering.
        
        This option is used only when metafile is rendered as vector graphics. When metafile is rendered
        to bitmap, WMF data is always used.
        
        The default value is ``True``."""
        ...
    
    @use_emf_embedded_to_wmf.setter
    def use_emf_embedded_to_wmf(self, value: bool):
        ...
    
    @property
    def emulate_raster_operations(self) -> bool:
        """Gets or sets a value determining whether or not the raster operations should be emulated.
        
        Specific raster operations could be used in metafiles. They can not be rendered directly to vector graphics.
        Emulating raster operations requires partial rasterization of the resulting vector graphics which may affect the
        metafile rendering performance.
        
        When this value is set to ``True``, Aspose.Words emulates the raster operations. The resulting output maybe
        partially rasterized and performance might be slower.
        
        When this value is set to ``False``, Aspose.Words does not emulate the raster operations. When Aspose.Words
        encounters a raster operation in a metafile it fallbacks to rendering the metafile into a bitmap by using the
        operating system.
        
        This option is used only when metafile is rendered as vector graphics.
        
        The default value is ``True``."""
        ...
    
    @emulate_raster_operations.setter
    def emulate_raster_operations(self, value: bool):
        ...
    
    @property
    def use_gdi_raster_operations_emulation(self) -> bool:
        """Gets or sets a value determining whether or not to use the GDI+ for raster operations emulation.
        
        Windows GDI+ library could be used to emulate raster operations. It provides support for all raster operation
        comparing to Aspose.Words own emulation but performance may be slower in some cases.
        
        When this value is set to ``True``, Aspose.Words uses GDI+ for raster operations emulation.
        
        When this value is set to ``False``, Aspose.Words uses its own implementation of raster operations emulation.
        
        This option is used only when metafile is rendered as vector graphics.
        
        The default value is ``False``."""
        ...
    
    @use_gdi_raster_operations_emulation.setter
    def use_gdi_raster_operations_emulation(self, value: bool):
        ...
    
    @property
    def emulate_rendering_to_size_on_page(self) -> bool:
        """Gets or sets a value determining whether metafile rendering emulates the display of the metafile according to the size on page
        or the display of the metafile in its default size.
        
        When metafiles are displayed in MS Word, some graphics may be scaled according to the actual metafile size in pixels.
        I.e. even zooming may affect the metafile display.
        
        When this value is set to ``True``, Aspose.Words emulates rendering according to the metafile size on page.
        The size in pixels is calculated from the metafile size on the page and the specified :attr:`MetafileRenderingOptions.emulate_rendering_to_size_on_page_resolution`.
        
        When this value is set to ``False``, Aspose.Words emulates metafile rendering to its default size in pixels.
        
        This option is used only when metafile is rendered as vector graphics.
        
        The default value is ``True``."""
        ...
    
    @emulate_rendering_to_size_on_page.setter
    def emulate_rendering_to_size_on_page(self, value: bool):
        ...
    
    @property
    def emulate_rendering_to_size_on_page_resolution(self) -> int:
        """Gets or sets the resolution in pixels per inch for the emulation of metafile rendering to the size on page.
        
        This option is used only when :attr:`MetafileRenderingOptions.emulate_rendering_to_size_on_page` is set to ``True``.
        
        The default value is 96. This is a default display resolution. I.e. metafile rendering will emulate the display of
        the metafile in MS Word with a 100% zoom factor."""
        ...
    
    @emulate_rendering_to_size_on_page_resolution.setter
    def emulate_rendering_to_size_on_page_resolution(self, value: int):
        ...
    
    ...

class OdtSaveOptions(aspose.words.saving.SaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.ODT` or
    :attr:`aspose.words.SaveFormat.OTT` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article.
    
    At the moment provides only the :attr:`OdtSaveOptions.save_format` property, but in the future will have
    other options added, such as an encryption password or digital signature settings."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.ODT` format."""
        ...
    
    @overload
    def __init__(self, password: str):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.ODT` format
        encrypted with a password."""
        ...
    
    @overload
    def __init__(self, save_format: aspose.words.SaveFormat):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.ODT` or
        :attr:`aspose.words.SaveFormat.OTT` format.
        
        :param save_format: Can be :attr:`aspose.words.SaveFormat.ODT` or :attr:`aspose.words.SaveFormat.OTT`."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can be :attr:`aspose.words.SaveFormat.ODT` or :attr:`aspose.words.SaveFormat.OTT`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def is_strict_schema11(self) -> bool:
        """Specifies whether export should correspond to ODT specification 1.1 strictly.
        OOo 3.0 displays files correctly when they contain elements and attributes of ODT 1.2.
        Use "false" for this purpose, or "true" for strict conformity of specification 1.1.
        The default value is ``False``."""
        ...
    
    @is_strict_schema11.setter
    def is_strict_schema11(self, value: bool):
        ...
    
    @property
    def measure_unit(self) -> aspose.words.saving.OdtSaveMeasureUnit:
        """Allows to specify units of measure to apply to document content.
        The default value is :attr:`OdtSaveMeasureUnit.CENTIMETERS`
        
        Open Office uses centimeters when specifying lengths, widths and other measurable formatting and
        content properties in documents whereas MS Office uses inches."""
        ...
    
    @measure_unit.setter
    def measure_unit(self, value: aspose.words.saving.OdtSaveMeasureUnit):
        ...
    
    @property
    def password(self) -> str:
        """Gets or sets a password to encrypt document.
        
        In order to save document without encryption this property should be ``None`` or empty string."""
        ...
    
    @password.setter
    def password(self, value: str):
        ...
    
    @property
    def digital_signature_details(self) -> aspose.words.saving.DigitalSignatureDetails:
        """Gets or sets :class:`DigitalSignatureDetails` object used to sign a document."""
        ...
    
    @digital_signature_details.setter
    def digital_signature_details(self, value: aspose.words.saving.DigitalSignatureDetails):
        ...
    
    ...

class OoxmlSaveOptions(aspose.words.saving.SaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.DOCX`,
    :attr:`aspose.words.SaveFormat.DOCM`, :attr:`aspose.words.SaveFormat.DOTX`, :attr:`aspose.words.SaveFormat.DOTM` or
    :attr:`aspose.words.SaveFormat.FLAT_OPC` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.DOCX` format."""
        ...
    
    @overload
    def __init__(self, save_format: aspose.words.SaveFormat):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.DOCX`,
        :attr:`aspose.words.SaveFormat.DOCM`, :attr:`aspose.words.SaveFormat.DOTX`, :attr:`aspose.words.SaveFormat.DOTM` or
        :attr:`aspose.words.SaveFormat.FLAT_OPC` format.
        
        :param save_format: Can be :attr:`aspose.words.SaveFormat.DOCX`, :attr:`aspose.words.SaveFormat.DOCM`,
                            :attr:`aspose.words.SaveFormat.DOTX`, :attr:`aspose.words.SaveFormat.DOTM` or :attr:`aspose.words.SaveFormat.FLAT_OPC`."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can be :attr:`aspose.words.SaveFormat.DOCX`, :attr:`aspose.words.SaveFormat.DOCM`,
        :attr:`aspose.words.SaveFormat.DOTX`, :attr:`aspose.words.SaveFormat.DOTM` or :attr:`aspose.words.SaveFormat.FLAT_OPC`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def password(self) -> str:
        """Gets/sets a password to encrypt document using ECMA376 Standard encryption algorithm.
        
        In order to save document without encryption this property should be ``None`` or empty string."""
        ...
    
    @password.setter
    def password(self, value: str):
        ...
    
    @property
    def compliance(self) -> aspose.words.saving.OoxmlCompliance:
        """Specifies the OOXML version for the output document.
        The default value is :attr:`OoxmlCompliance.ECMA376_2006`."""
        ...
    
    @compliance.setter
    def compliance(self, value: aspose.words.saving.OoxmlCompliance):
        ...
    
    @property
    def keep_legacy_control_chars(self) -> bool:
        """Keeps original representation of legacy control characters."""
        ...
    
    @keep_legacy_control_chars.setter
    def keep_legacy_control_chars(self, value: bool):
        ...
    
    @property
    def compression_level(self) -> aspose.words.saving.CompressionLevel:
        """Specifies the compression level used to save document.
        The default value is :attr:`CompressionLevel.NORMAL`."""
        ...
    
    @compression_level.setter
    def compression_level(self, value: aspose.words.saving.CompressionLevel):
        ...
    
    @property
    def zip_64_mode(self) -> aspose.words.saving.Zip64Mode:
        """Specifies whether or not to use ZIP64 format extensions for the output document.
        The default value is :attr:`Zip64Mode.NEVER`."""
        ...
    
    @zip_64_mode.setter
    def zip_64_mode(self, value: aspose.words.saving.Zip64Mode):
        ...
    
    @property
    def digital_signature_details(self) -> aspose.words.saving.DigitalSignatureDetails:
        """Gets or sets :class:`DigitalSignatureDetails` object used to sign a document."""
        ...
    
    @digital_signature_details.setter
    def digital_signature_details(self, value: aspose.words.saving.DigitalSignatureDetails):
        ...
    
    ...

class OutlineOptions:
    """Allows to specify outline options.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def create_missing_outline_levels(self) -> bool:
        """Gets or sets a value determining whether or not to create missing outline levels when the document is
        exported.
        
        Default value for this property is ``False``."""
        ...
    
    @create_missing_outline_levels.setter
    def create_missing_outline_levels(self, value: bool):
        ...
    
    @property
    def headings_outline_levels(self) -> int:
        """Specifies how many levels of headings (paragraphs formatted with the Heading styles) to include in the
        document outline.
        
        Specify 0 for no headings in the outline; specify 1 for one level of headings in the outline and so on.
        
        Default is 0. Valid range is 0 to 9."""
        ...
    
    @headings_outline_levels.setter
    def headings_outline_levels(self, value: int):
        ...
    
    @property
    def expanded_outline_levels(self) -> int:
        """Specifies how many levels in the document outline to show expanded when the file is viewed.
        
        Note that this options will not work when saving to XPS.
        
        Specify 0 and the document outline will be collapsed; specify 1 and the first level items
        in the outline will be expanded and so on.
        
        Default is 0. Valid range is 0 to 9."""
        ...
    
    @expanded_outline_levels.setter
    def expanded_outline_levels(self, value: int):
        ...
    
    @property
    def default_bookmarks_outline_level(self) -> int:
        """Specifies the default level in the document outline at which to display Word bookmarks.
        
        Individual bookmarks level could be specified using :attr:`OutlineOptions.bookmarks_outline_levels` property.
        
        Specify 0 and Word bookmarks will not be displayed in the document outline.
        Specify 1 and Word bookmarks will be displayed in the document outline at level 1; 2 for level 2 and so on.
        
        Default is 0. Valid range is 0 to 9."""
        ...
    
    @default_bookmarks_outline_level.setter
    def default_bookmarks_outline_level(self, value: int):
        ...
    
    @property
    def bookmarks_outline_levels(self) -> aspose.words.saving.BookmarksOutlineLevelCollection:
        """Allows to specify individual bookmarks outline level.
        
        If bookmark level is not specified in this collection then :attr:`OutlineOptions.default_bookmarks_outline_level` value is used."""
        ...
    
    @property
    def create_outlines_for_headings_in_tables(self) -> bool:
        """Specifies whether or not to create outlines for headings (paragraphs formatted with the Heading styles) inside tables.
        
        Default value is ``False``."""
        ...
    
    @create_outlines_for_headings_in_tables.setter
    def create_outlines_for_headings_in_tables(self, value: bool):
        ...
    
    ...

class PageRange:
    """Represents a continuous range of pages.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    def __init__(self, from_address: int, to: int):
        """Creates a new page range object.
        
        :param from_address: The starting page zero-based index.
        :param to: The ending page zero-based index.
                   If it exceeds the index of the last page in the document,
                   it is truncated to fit in the document on rendering.
        
        int.MaxValue C# constant means the last page in the document."""
        ...
    
    ...

class PageSavingArgs:
    """Provides data for the :meth:`IPageSavingCallback.page_saving` event.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def page_stream(self) -> io.BytesIO:
        """Allows to specify the stream where the document page will be saved to.
        
        This property allows you to save document pages to streams instead of files.
        
        The default value is ``None``. When this property is ``None``, the document page
        will be saved to a file specified in the :attr:`PageSavingArgs.page_file_name` property.
        
        If both :attr:`PageSavingArgs.page_stream` and :attr:`PageSavingArgs.page_file_name` are set, then PageStream will be used."""
        ...
    
    @page_stream.setter
    def page_stream(self, value: io.BytesIO):
        ...
    
    @property
    def keep_page_stream_open(self) -> bool:
        """Specifies whether Aspose.Words should keep the stream open or close it after saving a document page.
        
        Default is ``False`` and Aspose.Words will close the stream you provided
        in the :attr:`PageSavingArgs.page_stream` property after writing a document page into it.
        Specify ``True`` to keep the stream open."""
        ...
    
    @keep_page_stream_open.setter
    def keep_page_stream_open(self, value: bool):
        ...
    
    @property
    def page_file_name(self) -> str:
        """Gets or sets the file name where the document page will be saved to.
        
        If not specified then page file name and path will be generated automatically using original file name."""
        ...
    
    @page_file_name.setter
    def page_file_name(self, value: str):
        ...
    
    @property
    def page_index(self) -> int:
        """Current page index."""
        ...
    
    ...

class PageSet:
    """Describes a random set of pages.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    @overload
    def __init__(self, page: int):
        """Creates an one-page set based on exact page index.
        
        :param page: Zero-based index of the page.
        
        If a page is encountered that is not in the document, an exception will be thrown during rendering.
        int.MaxValue C# constant means the last page in the document."""
        ...
    
    @overload
    def __init__(self, pages: List[int]):
        """Creates a page set based on exact page indices.
        
        :param pages: Zero-based indices of pages.
        
        If a page is encountered that is not in the document, an exception will be thrown during rendering.
        int.MaxValue C# constant means the last page in the document."""
        ...
    
    @overload
    def __init__(self, ranges: List[aspose.words.saving.PageRange]):
        """Creates a page set based on ranges.
        
        :param ranges: Array of page ranges.
        
        If a range is encountered that starts after the last page in the document,
        an exception will be thrown during rendering.
        All ranges that end after the last page are truncated to fit in the document."""
        ...
    
    all: aspose.words.saving.PageSet
    
    even: aspose.words.saving.PageSet
    
    odd: aspose.words.saving.PageSet
    
    ...

class PclSaveOptions(aspose.words.saving.FixedPageSaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.PCL` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    def add_printer_font(self, font_full_name: str, font_pcl_name: str) -> None:
        """Adds information about font that is uploaded to the printer by manufacturer.
        
        :param font_full_name: Full name of the font (e.g. "Times New Roman Bold Italic").
        :param font_pcl_name: Name of the font that is used in Pcl document.
        
        There are 52 fonts that are to be built in any printer according to Pcl specification.
        However manufactures can add some other fonts to their devices."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.PCL`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def rasterize_transformed_elements(self) -> bool:
        """Gets or sets a value determining whether or not complex transformed elements
        should be rasterized before saving to PCL document.
        Default is ``True``.
        
        PCL doesn't support some kind of transformations that are used by Aspose Words.
        E.g. rotated, skewed images and texture brushes. To properly render such elements
        rasterization process is used, i.e. saving to image and clipping.
        This process can take additional time and memory.
        If flag is set to ``False``, some content in output may be different
        as compared with the source document."""
        ...
    
    @rasterize_transformed_elements.setter
    def rasterize_transformed_elements(self, value: bool):
        ...
    
    @property
    def fallback_font_name(self) -> str:
        """Name of the font that will be used
        if no expected font is found in printer and built-in fonts collections.
        
        If no fallback is found, a warning is generated and "Arial" font is used."""
        ...
    
    @fallback_font_name.setter
    def fallback_font_name(self, value: str):
        ...
    
    ...

class PdfDigitalSignatureDetails:
    """Contains details for signing a PDF document with a digital signature.
    
    At the moment digitally signing PDF documents is only available on .NET 3.5 or higher.
    
    To digitally sign a PDF document when it is created by Aspose.Words, set the :attr:`PdfSaveOptions.digital_signature_details`
    property to a valid :class:`PdfDigitalSignatureDetails` object and then save the document in the PDF format passing
    the :class:`PdfSaveOptions` as a parameter into the :meth:`aspose.words.Document.save` method.
    
    Aspose.Words creates a PKCS#7 signature over the whole PDF document and uses the "Adobe.PPKMS" filter and
    "adbe.pkcs7.sha1" subfilter when creating a digital signature."""
    
    @overload
    def __init__(self):
        """Initializes an instance of this class."""
        ...
    
    @overload
    def __init__(self, certificate_holder: aspose.words.digitalsignatures.CertificateHolder, reason: str, location: str, signature_date: datetime.datetime):
        """Initializes an instance of this class.
        
        :param certificate_holder: A certificate holder which contains the certificate itself.
        :param reason: The reason for signing.
        :param location: The location of signing.
        :param signature_date: The date and time of signing."""
        ...
    
    @property
    def certificate_holder(self) -> aspose.words.digitalsignatures.CertificateHolder:
        """Returns the certificate holder object that contains the certificate was used to sign the document."""
        ...
    
    @certificate_holder.setter
    def certificate_holder(self, value: aspose.words.digitalsignatures.CertificateHolder):
        ...
    
    @property
    def reason(self) -> str:
        """Gets or sets the reason for the signing.
        
        The default value is ``None``."""
        ...
    
    @reason.setter
    def reason(self, value: str):
        ...
    
    @property
    def location(self) -> str:
        """Gets or sets the location of the signing.
        
        The default value is ``None``."""
        ...
    
    @location.setter
    def location(self, value: str):
        ...
    
    @property
    def signature_date(self) -> datetime.datetime:
        """Gets or sets the date of the signing.
        
        The default value is the current time.
        
        This value will appear in the digital signature as an unverified computer time."""
        ...
    
    @signature_date.setter
    def signature_date(self, value: datetime.datetime):
        ...
    
    @property
    def hash_algorithm(self) -> aspose.words.saving.PdfDigitalSignatureHashAlgorithm:
        """Gets or sets the hash algorithm.
        
        The default value is the SHA-256 algorithm."""
        ...
    
    @hash_algorithm.setter
    def hash_algorithm(self, value: aspose.words.saving.PdfDigitalSignatureHashAlgorithm):
        ...
    
    @property
    def timestamp_settings(self) -> aspose.words.saving.PdfDigitalSignatureTimestampSettings:
        """Gets or sets the digital signature timestamp settings.
        
        The default value is ``None`` and the digital signature will not be time-stamped.
        When this property is set to a valid :class:`PdfDigitalSignatureTimestampSettings` object,
        then the digital signature in the PDF document will be time-stamped."""
        ...
    
    @timestamp_settings.setter
    def timestamp_settings(self, value: aspose.words.saving.PdfDigitalSignatureTimestampSettings):
        ...
    
    ...

class PdfDigitalSignatureTimestampSettings:
    """Contains settings of the digital signature timestamp.
    To learn more, visit the `Work with Digital Signatures <https://docs.aspose.com/words/python-net/working-with-digital-signatures/>` documentation article."""
    
    @overload
    def __init__(self):
        """Initializes an instance of this class."""
        ...
    
    @overload
    def __init__(self, server_url: str, user_name: str, password: str):
        """Initializes an instance of this class.
        
        :param server_url: Timestamp server URL.
        :param user_name: Timestamp server user name.
        :param password: Timestamp server password."""
        ...
    
    @overload
    def __init__(self, server_url: str, user_name: str, password: str, timeout: datetime.timespan):
        """Initializes an instance of this class.
        
        :param server_url: Timestamp server URL.
        :param user_name: Timestamp server user name.
        :param password: Timestamp server password.
        :param timeout: Time-out value for accessing timestamp server."""
        ...
    
    @property
    def server_url(self) -> str:
        """Timestamp server URL.
        
        The default value is ``None``.
        If ``None``, then the digital signature will not be time-stamped."""
        ...
    
    @server_url.setter
    def server_url(self, value: str):
        ...
    
    @property
    def user_name(self) -> str:
        """Timestamp server user name.
        
        The default value is ``None``."""
        ...
    
    @user_name.setter
    def user_name(self, value: str):
        ...
    
    @property
    def password(self) -> str:
        """Timestamp server password.
        
        The default value is ``None``."""
        ...
    
    @password.setter
    def password(self, value: str):
        ...
    
    @property
    def timeout(self) -> datetime.timespan:
        """Time-out value for accessing timestamp server.
        
        The default value is 100 seconds."""
        ...
    
    @timeout.setter
    def timeout(self, value: datetime.timespan):
        ...
    
    ...

class PdfEncryptionDetails:
    """Contains details for encrypting and access permissions for a PDF document.
    To learn more, visit the `Protect or Encrypt a Document <https://docs.aspose.com/words/python-net/protect-or-encrypt-a-document/>` documentation article."""
    
    @overload
    def __init__(self, user_password: str, owner_password: str):
        """Initializes an instance of this class."""
        ...
    
    @overload
    def __init__(self, user_password: str, owner_password: str, permissions: aspose.words.saving.PdfPermissions):
        """Initializes an instance of this class."""
        ...
    
    @property
    def user_password(self) -> str:
        """Specifies the user password required for opening the encrypted PDF document.
        
        The user password will be required to open an encrypted PDF document for viewing. The permissions specified in
        :attr:`PdfEncryptionDetails.permissions` will be enforced by the reader software.
        
        The user password can be ``None`` or empty string, in this case no password will be required from the user when
        opening the PDF document. The user password cannot be the same as the owner password."""
        ...
    
    @user_password.setter
    def user_password(self, value: str):
        ...
    
    @property
    def owner_password(self) -> str:
        """Specifies the owner password for the encrypted PDF document.
        
        The owner password allows the user to open an encrypted PDF document without any access restrictions
        specified in :attr:`PdfEncryptionDetails.permissions`.
        
        The owner password cannot be the same as the user password."""
        ...
    
    @owner_password.setter
    def owner_password(self, value: str):
        ...
    
    @property
    def permissions(self) -> aspose.words.saving.PdfPermissions:
        """Specifies the operations that are allowed to a user on an encrypted PDF document.
        The default value is :attr:`PdfPermissions.DISALLOW_ALL`."""
        ...
    
    @permissions.setter
    def permissions(self, value: aspose.words.saving.PdfPermissions):
        ...
    
    ...

class PdfSaveOptions(aspose.words.saving.FixedPageSaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.PDF` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        """Initializes a new instance of this class that can be used to save a document in the
        :attr:`aspose.words.SaveFormat.PDF` format."""
        ...
    
    def clone(self) -> aspose.words.saving.PdfSaveOptions:
        """Creates a deep clone of this object."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.PDF`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def dml_effects_rendering_mode(self) -> aspose.words.saving.DmlEffectsRenderingMode:
        """Gets or sets a value determining how DrawingML effects are rendered.
        
        The default value is :attr:`DmlEffectsRenderingMode.SIMPLIFIED`.
        This property is used when the document is exported to fixed page formats.
        
        If :attr:`PdfSaveOptions.compliance` is set to :attr:`PdfCompliance.PDF_A1A` or :attr:`PdfCompliance.PDF_A1B`,
        property always returns :attr:`DmlEffectsRenderingMode.NONE`."""
        ...
    
    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, value: aspose.words.saving.DmlEffectsRenderingMode):
        ...
    
    @property
    def jpeg_quality(self) -> int:
        """Gets or sets a value determining the quality of the JPEG images inside PDF document.
        
        The default value is 100.
        
        This property is used in conjunction with the :attr:`PdfSaveOptions.image_compression` option.
        
        Has effect only when a document contains JPEG images.
        
        Use this property to get or set the quality of the images inside a document when saving in PDF format.
        The value may vary from 0 to 100 where 0 means worst quality but maximum compression and 100
        means best quality but minimum compression.
        If quality is 100 and source image is JPEG, it means no compression - original bytes will be saved."""
        ...
    
    @jpeg_quality.setter
    def jpeg_quality(self, value: int):
        ...
    
    @property
    def outline_options(self) -> aspose.words.saving.OutlineOptions:
        """Allows to specify outline options.
        
        Outlines can be created from headings and bookmarks.
        
        For headings outline level is determined by the heading level.
        
        It is possible to set the max heading level to be included into outlines or disable heading outlines at all.
        
        For bookmarks outline level may be set in options as a default value for all bookmarks or as individual values for particular bookmarks.
        
        Also, outlines can be exported to XPS format by using the same :attr:`PdfSaveOptions.outline_options` class."""
        ...
    
    @property
    def text_compression(self) -> aspose.words.saving.PdfTextCompression:
        """Specifies compression type to be used for all textual content in the document.
        
        Default is :attr:`PdfTextCompression.FLATE`.
        
        Significantly increases output size when saving a document without compression."""
        ...
    
    @text_compression.setter
    def text_compression(self, value: aspose.words.saving.PdfTextCompression):
        ...
    
    @property
    def preserve_form_fields(self) -> bool:
        """Specifies whether to preserve Microsoft Word form fields as form fields in PDF or convert them to text.
        Default is ``False``.
        
        Microsoft Word form fields include text input, drop down and check box controls.
        
        When set to ``False``, these fields will be exported as text to PDF. When set to ``True``,
        these fields will be exported as PDF form fields.
        
        When exporting form fields to PDF as form fields, some formatting loss might occur because PDF form
        fields do not support all features of Microsoft Word form fields.
        
        Also, the output size depends on the content size because editable forms in Microsoft Word are
        inline objects.
        
        Editable forms are prohibited by PDF/A compliance. ``False`` value will be used automatically
        when saving to PDF/A.
        
        Form fields are not supported when saving to PDF/UA. ``False`` value will be used automatically."""
        ...
    
    @preserve_form_fields.setter
    def preserve_form_fields(self, value: bool):
        ...
    
    @property
    def create_note_hyperlinks(self) -> bool:
        """Specifies whether to convert footnote/endnote references in main text story into active hyperlinks.
        When clicked the hyperlink will lead to the corresponding footnote/endnote.
        Default is ``False``."""
        ...
    
    @create_note_hyperlinks.setter
    def create_note_hyperlinks(self, value: bool):
        ...
    
    @property
    def encryption_details(self) -> aspose.words.saving.PdfEncryptionDetails:
        """Gets or sets the details for encrypting the output PDF document.
        
        The default value is ``None`` and the output document will not be encrypted.
        When this property is set to a valid :class:`PdfEncryptionDetails` object,
        then the output PDF document will be encrypted.
        
        AES-128 encryption algorithm is used when saving to PDF 1.7 based compliance (including PDF/UA-1).
        AES-256 encryption algorithm is used when saving to PDF 2.0 based compliance.
        
        Encryption is prohibited by PDF/A compliance. This option will be ignored when saving to PDF/A.
        
        :attr:`PdfPermissions.CONTENT_COPY_FOR_ACCESSIBILITY` permission is required by PDF/UA compliance
        if the output document is encrypted. This permission will automatically used when saving to PDF/UA.
        
        :attr:`PdfPermissions.CONTENT_COPY_FOR_ACCESSIBILITY` permission is deprecated in PDF 2.0 format.
        This permission will be ignored when saving to PDF 2.0."""
        ...
    
    @encryption_details.setter
    def encryption_details(self, value: aspose.words.saving.PdfEncryptionDetails):
        ...
    
    @property
    def digital_signature_details(self) -> aspose.words.saving.PdfDigitalSignatureDetails:
        """Gets or sets the details for signing the output PDF document.
        
        The default value is ``None`` and the output document will not be signed.
        When this property is set to a valid :class:`PdfDigitalSignatureDetails` object,
        then the output PDF document will be digitally signed."""
        ...
    
    @digital_signature_details.setter
    def digital_signature_details(self, value: aspose.words.saving.PdfDigitalSignatureDetails):
        ...
    
    @property
    def embed_full_fonts(self) -> bool:
        """Controls how fonts are embedded into the resulting PDF documents.
        
        The default value is ``False``, which means the fonts are subsetted before embedding.
        Subsetting is useful if you want to keep the output file size smaller. Subsetting removes all
        unused glyphs from a font.
        
        When this value is set to ``True``, a complete font file is embedded into PDF without
        subsetting. This will result in larger output files, but can be a useful option when you want to
        edit the resulting PDF later (e.g. add more text).
        
        Some fonts are large (several megabytes) and embedding them without subsetting
        will result in large output documents."""
        ...
    
    @embed_full_fonts.setter
    def embed_full_fonts(self, value: bool):
        ...
    
    @property
    def font_embedding_mode(self) -> aspose.words.saving.PdfFontEmbeddingMode:
        """Specifies the font embedding mode.
        
        The default value is :attr:`PdfFontEmbeddingMode.EMBED_ALL`.
        
        This setting works only for the text in ANSI (Windows-1252) encoding. If the document contains
        non-ANSI text then corresponding fonts will be embedded regardless of this setting.
        
        PDF/A and PDF/UA compliance requires all fonts to be embedded.
        :attr:`PdfFontEmbeddingMode.EMBED_ALL` value will be used automatically when saving to
        PDF/A and PDF/UA."""
        ...
    
    @font_embedding_mode.setter
    def font_embedding_mode(self, value: aspose.words.saving.PdfFontEmbeddingMode):
        ...
    
    @property
    def use_core_fonts(self) -> bool:
        """Gets or sets a value determining whether or not to substitute TrueType fonts Arial, Times New Roman,
        Courier New and Symbol with core PDF Type 1 fonts.
        
        The default value is ``False``. When this value is set to ``True`` Arial, Times New Roman,
        Courier New and Symbol fonts are replaced in PDF document with corresponding core Type 1 font.
        
        Core PDF fonts, or their font metrics and suitable substitution fonts, are required to be available to any
        PDF viewer application.
        
        This setting works only for the text in ANSI (Windows-1252) encoding. Non-ANSI text will be written
        with embedded TrueType font regardless of this setting.
        
        PDF/A and PDF/UA compliance requires all fonts to be embedded. ``False`` value will be used
        automatically when saving to PDF/A and PDF/UA.
        
        Core fonts are not supported when saving to PDF 2.0 format. ``False`` value will be used
        automatically when saving to PDF 2.0.
        
        This option has a higher priority then :attr:`PdfSaveOptions.font_embedding_mode` option."""
        ...
    
    @use_core_fonts.setter
    def use_core_fonts(self, value: bool):
        ...
    
    @property
    def custom_properties_export(self) -> aspose.words.saving.PdfCustomPropertiesExport:
        """Gets or sets a value determining the way :attr:`aspose.words.Document.custom_document_properties` are exported to PDF file.
        
        Default value is :attr:`PdfCustomPropertiesExport.NONE`.
        
        :attr:`PdfCustomPropertiesExport.METADATA` value is not supported when saving to PDF/A.
        :attr:`PdfCustomPropertiesExport.STANDARD` will be used instead for PDF/A-1 and PDF/A-2 and
        :attr:`PdfCustomPropertiesExport.NONE` for PDF/A-4.
        
        :attr:`PdfCustomPropertiesExport.STANDARD` value is not supported when saving to PDF 2.0.
        :attr:`PdfCustomPropertiesExport.METADATA` will be used instead."""
        ...
    
    @custom_properties_export.setter
    def custom_properties_export(self, value: aspose.words.saving.PdfCustomPropertiesExport):
        ...
    
    @property
    def zoom_behavior(self) -> aspose.words.saving.PdfZoomBehavior:
        """Gets or sets a value determining what type of zoom should be applied when a document is opened with a PDF viewer.
        
        The default value is :attr:`PdfZoomBehavior.NONE`, i.e. no fit is applied."""
        ...
    
    @zoom_behavior.setter
    def zoom_behavior(self, value: aspose.words.saving.PdfZoomBehavior):
        ...
    
    @property
    def zoom_factor(self) -> int:
        """Gets or sets a value determining zoom factor (in percentages) for a document.
        
        This value is used only if :attr:`PdfSaveOptions.zoom_behavior` is set to :attr:`PdfZoomBehavior.ZOOM_FACTOR`."""
        ...
    
    @zoom_factor.setter
    def zoom_factor(self, value: int):
        ...
    
    @property
    def image_compression(self) -> aspose.words.saving.PdfImageCompression:
        """Specifies compression type to be used for all images in the document.
        
        Default is :attr:`PdfImageCompression.AUTO`.
        
        Using :attr:`PdfImageCompression.JPEG` lets you control the quality of images in the output document through the :attr:`PdfSaveOptions.jpeg_quality` property.
        
        Using :attr:`PdfImageCompression.JPEG` provides the fastest conversion speed when compared to the performance of other compression types,
        but in this case, there is lossy JPEG compression.
        
        Using :attr:`PdfImageCompression.AUTO` lets to control the quality of Jpeg in the output document through the :attr:`PdfSaveOptions.jpeg_quality` property,
        but for other formats, raw pixel data is extracted and saved with Flate compression.
        This case is slower than Jpeg conversion but lossless."""
        ...
    
    @image_compression.setter
    def image_compression(self, value: aspose.words.saving.PdfImageCompression):
        ...
    
    @property
    def open_hyperlinks_in_new_window(self) -> bool:
        """Gets or sets a value determining whether hyperlinks in the output Pdf document
        are forced to be opened in a new window (or tab) of a browser.
        
        The default value is ``False``. When this value is set to ``True``
        hyperlinks are saved using JavaScript code.
        JavaScript code is ``app.launchURL("URL", true);``,
        where ``URL`` is a hyperlink.
        
        Note that if this option is set to ``True`` hyperlinks can't work
        in some PDF readers e.g. Chrome, Firefox.
        
        JavaScript actions are prohibited by PDF/A-1 and PDF/A-2 compliance. ``False`` will be used automatically when
        saving to PDF/A-1 and PDF/A-2."""
        ...
    
    @open_hyperlinks_in_new_window.setter
    def open_hyperlinks_in_new_window(self, value: bool):
        ...
    
    @property
    def export_document_structure(self) -> bool:
        """Gets or sets a value determining whether or not to export document structure.
        
        This value is ignored when saving to PDF/A-1a, PDF/A-2a and PDF/UA-1 because document structure is required for this compliance.
        
        Note that exporting the document structure significantly increases the memory consumption, especially
        for the large documents."""
        ...
    
    @export_document_structure.setter
    def export_document_structure(self, value: bool):
        ...
    
    @property
    def export_language_to_span_tag(self) -> bool:
        """Gets or sets a value determining whether or not to create a "Span" tag in the document structure to export the text language.
        
        Default value is ``False`` and "Lang" attribute is attached to a marked-content sequence in a page content stream.
        
        When the value is ``True`` "Span" tag is created for the text with non-default language
        and "Lang" attribute is attached to this tag.
        
        This value is ignored when :attr:`PdfSaveOptions.export_document_structure` is ``False``."""
        ...
    
    @export_language_to_span_tag.setter
    def export_language_to_span_tag(self, value: bool):
        ...
    
    @property
    def export_paragraph_graphics_to_artifact(self) -> bool:
        """Gets or sets a value determining whether a paragraph graphic should be marked as an artifact.
        
        Default value is ``False`` and paragraph graphics (underlines, text emphasis, etc.)
        will be marked as "Span" in the logical structure of the document.
        
        When the value is ``True`` the paragraph graphics will be marked as "Artifact".
        
        This value is ignored when :attr:`PdfSaveOptions.export_document_structure` is ``False``."""
        ...
    
    @export_paragraph_graphics_to_artifact.setter
    def export_paragraph_graphics_to_artifact(self, value: bool):
        ...
    
    @property
    def use_book_fold_printing_settings(self) -> bool:
        """Gets or sets a boolean value indicating whether the document should be saved using a booklet printing layout,
        if it is specified via :attr:`aspose.words.PageSetup.multiple_pages`.
        
        If this option is specified, :attr:`FixedPageSaveOptions.page_set` is ignored when saving.
        This behavior matches MS Word.
        If book fold printing settings are not specified in page setup, this option will have no effect."""
        ...
    
    @use_book_fold_printing_settings.setter
    def use_book_fold_printing_settings(self, value: bool):
        ...
    
    @property
    def downsample_options(self) -> aspose.words.saving.DownsampleOptions:
        """Allows to specify downsample options."""
        ...
    
    @downsample_options.setter
    def downsample_options(self, value: aspose.words.saving.DownsampleOptions):
        ...
    
    @property
    def page_layout(self) -> aspose.words.saving.PdfPageLayout:
        """Specifies the page layout to be used when the document is opened in a PDF reader.
        
        The default value is :attr:`PdfPageLayout.SINGLE_PAGE`."""
        ...
    
    @page_layout.setter
    def page_layout(self, value: aspose.words.saving.PdfPageLayout):
        ...
    
    @property
    def page_mode(self) -> aspose.words.saving.PdfPageMode:
        """Specifies how the PDF document should be displayed when opened in a PDF reader.
        
        The default value is :attr:`PdfPageMode.USE_OUTLINES`."""
        ...
    
    @page_mode.setter
    def page_mode(self, value: aspose.words.saving.PdfPageMode):
        ...
    
    @property
    def image_color_space_export_mode(self) -> aspose.words.saving.PdfImageColorSpaceExportMode:
        """Specifies how the color space will be selected for the images in PDF document.
        
        The default value is :attr:`PdfImageColorSpaceExportMode.AUTO`.
        
        If :attr:`PdfImageColorSpaceExportMode.SIMPLE_CMYK` value is specified,
        :attr:`PdfSaveOptions.image_compression` option is ignored and
        Flate compression is used for all images in the document.
        
        :attr:`PdfImageColorSpaceExportMode.SIMPLE_CMYK` value is not supported when saving to PDF/A.
        :attr:`PdfImageColorSpaceExportMode.AUTO` value will be used instead."""
        ...
    
    @image_color_space_export_mode.setter
    def image_color_space_export_mode(self, value: aspose.words.saving.PdfImageColorSpaceExportMode):
        ...
    
    @property
    def preblend_images(self) -> bool:
        """Gets or sets a value determining whether or not to preblend transparent images with black background color.
        
        Preblending images may improve PDF document visual appearance in Adobe Reader and remove anti-aliasing artifacts.
        
        In order to properly display preblended images, PDF viewer application must support /Matte entry in soft-mask image dictionary.
        Also preblending images may decrease PDF rendering performance.
        
        The default value is ``False``."""
        ...
    
    @preblend_images.setter
    def preblend_images(self, value: bool):
        ...
    
    @property
    def display_doc_title(self) -> bool:
        """A flag specifying whether the window’s title bar should display the document title taken from
        the Title entry of the document information dictionary.
        
        If ``False``, the title bar should instead display the name of the PDF file containing the document.
        
        This flag is required by PDF/UA compliance. ``True`` value will be used automatically when saving
        to PDF/UA.
        
        The default value is ``False``."""
        ...
    
    @display_doc_title.setter
    def display_doc_title(self, value: bool):
        ...
    
    @property
    def header_footer_bookmarks_export_mode(self) -> aspose.words.saving.HeaderFooterBookmarksExportMode:
        """Determines how bookmarks in headers/footers are exported.
        
        The default value is :attr:`HeaderFooterBookmarksExportMode.ALL`.
        
        This property is used in conjunction with the :attr:`PdfSaveOptions.outline_options` option."""
        ...
    
    @header_footer_bookmarks_export_mode.setter
    def header_footer_bookmarks_export_mode(self, value: aspose.words.saving.HeaderFooterBookmarksExportMode):
        ...
    
    @property
    def additional_text_positioning(self) -> bool:
        """A flag specifying whether to write additional text positioning operators or not.
        
        If ``True``, additional text positioning operators are written to the output PDF. This may help to overcome
        issues with inaccurate text positioning with some printers. The downside is the increased PDF document size.
        
        The default value is ``False``."""
        ...
    
    @additional_text_positioning.setter
    def additional_text_positioning(self, value: bool):
        ...
    
    @property
    def interpolate_images(self) -> bool:
        """A flag indicating whether image interpolation shall be performed by a conforming reader.
        When ``False`` is specified, the flag is not written to the output document and
        the default behaviour of reader is used instead.
        
        When the resolution of a source image is significantly lower than that of the output device,
        each source sample covers many device pixels. As a result, images can appear jaggy or blocky.
        These visual artifacts can be reduced by applying an image interpolation algorithm during rendering.
        Instead of painting all pixels covered by a source sample with the same color, image interpolation
        attempts to produce a smooth transition between adjacent sample values.
        
        A conforming Reader may choose to not implement this feature of PDF,
        or may use any specific implementation of interpolation that it wishes.
        
        The default value is ``False``.
        
        Interpolation flag is prohibited by PDF/A compliance. ``False`` value will be used automatically
        when saving to PDF/A."""
        ...
    
    @interpolate_images.setter
    def interpolate_images(self, value: bool):
        ...
    
    @property
    def compliance(self) -> aspose.words.saving.PdfCompliance:
        """Specifies the PDF standards compliance level for output documents.
        
        Default is :attr:`PdfCompliance.PDF17`."""
        ...
    
    @compliance.setter
    def compliance(self, value: aspose.words.saving.PdfCompliance):
        ...
    
    @property
    def cache_background_graphics(self) -> bool:
        """Gets or sets a value determining whether or not to cache graphics placed in document's background.
        
        Default value is ``True`` and background graphics are written to the PDF document as an xObject.
        
        When the value is ``False`` background graphics are not cached.
        
        Some shapes are not supported for caching(shapes with fields, bookmarks, HRefs).
        
        Document background graphic is various shapes, charts, images placed in the footer or header,
        well as background and border of a page."""
        ...
    
    @cache_background_graphics.setter
    def cache_background_graphics(self, value: bool):
        ...
    
    @property
    def embed_attachments(self) -> bool:
        """Gets or sets a value determining whether or not to embed attachments to the PDF document.
        
        Default value is ``False`` and attachments are not embedded.
        
        When the value is ``True`` attachments are embedded to the PDF document.
        
        Embedding attachments is not supported when saving to PDF/A and PDF/UA compliance.
        ``False`` value will be used automatically.
        
        Embedding attachments is not supported when encryption is enabled. ``False`` value
        will be used automatically."""
        ...
    
    @embed_attachments.setter
    def embed_attachments(self, value: bool):
        ...
    
    ...

class PsSaveOptions(aspose.words.saving.FixedPageSaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.PS` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.PS`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def use_book_fold_printing_settings(self) -> bool:
        """Gets or sets a boolean value indicating whether the document should be saved using a booklet printing layout,
        if it is specified via :attr:`aspose.words.PageSetup.multiple_pages`.
        
        If this option is specified, :attr:`FixedPageSaveOptions.page_set` is ignored when saving.
        This behavior matches MS Word.
        If book fold printing settings are not specified in page setup, this option will have no effect."""
        ...
    
    @use_book_fold_printing_settings.setter
    def use_book_fold_printing_settings(self, value: bool):
        ...
    
    ...

class ResourceSavingArgs:
    """Provides data for the :meth:`IResourceSavingCallback.resource_saving` event.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article.
    
    By default, when Aspose.Words saves a document to fixed page HTML or SVG, it saves each resource into
    a separate file. Aspose.Words uses the document file name and a unique number to generate unique file name
    for each resource found in the document.
    
    :class:`ResourceSavingArgs` allows to redefine how resource file names are generated or to
    completely circumvent saving of resources into files by providing your own stream objects.
    
    To apply your own logic for generating resource file names use the
    :attr:`ResourceSavingArgs.resource_file_name` property.
    
    To save resources into streams instead of files, use the :attr:`ResourceSavingArgs.resource_stream` property."""
    
    @property
    def document(self) -> aspose.words.Document:
        """Gets the document object that is currently being saved."""
        ...
    
    @property
    def resource_file_name(self) -> str:
        """Gets or sets the file name (without path) where the resource will be saved to.
        
        This property allows you to redefine how the resource file names are generated
        during export to fixed page HTML or SVG.
        
        When the event is fired, this property contains the file name that was generated
        by Aspose.Words. You can change the value of this property to save the resource into a
        different file. Note that file names must be unique.
        
        Aspose.Words automatically generates a unique file name for every resource when
        exporting to fixed page HTML or SVG format. How the resource file name is generated
        depends on whether you save the document to a file or to a stream.
        
        When saving a document to a file, the generated resource file name looks like
        *\<document base file name\>.\<image number\>.\<extension\>*.
        
        When saving a document to a stream, the generated resource file name looks like
        *Aspose.Words.\<document guid\>.\<image number\>.\<extension\>*.
        
        :attr:`ResourceSavingArgs.resource_file_name` must contain only the file name without the path.
        Aspose.Words determines the path for saving and the value of the ``src`` attribute for writing
        to fixed page HTML or SVG using the document file name, the :attr:`HtmlFixedSaveOptions.resources_folder`
        or :attr:`SvgSaveOptions.resources_folder` and :attr:`HtmlFixedSaveOptions.resources_folder_alias`
        or :attr:`SvgSaveOptions.resources_folder_alias` properties.
        
        :attr:`HtmlFixedSaveOptions.resources_folder`
        :attr:`SvgSaveOptions.resources_folder`
        :attr:`HtmlFixedSaveOptions.resources_folder_alias`
        :attr:`SvgSaveOptions.resources_folder_alias`"""
        ...
    
    @resource_file_name.setter
    def resource_file_name(self, value: str):
        ...
    
    @property
    def resource_file_uri(self) -> str:
        """Gets or sets the uniform resource identifier (URI) used to reference the resource file from the document.
        
        This property allows you to change URIs of resource files exported to fixed page HTML or SVG documents.
        
        Aspose.Words automatically generates an URI for every resource file during export to fixed page HTML
        or SVG format. The generated URIs reference resource files saved by Aspose.Words. However, the URIs can be
        incorrect if resource files are to be moved to other location or if resource files are saved to streams.
        This property allows to correct URIs in these cases.
        
        When the event is fired, this property contains the URI that was generated
        by Aspose.Words. You can change the value of this property to provide a custom URI for the resource file.
        
        :attr:`HtmlFixedSaveOptions.resources_folder`
        :attr:`SvgSaveOptions.resources_folder`
        :attr:`HtmlFixedSaveOptions.resources_folder_alias`
        :attr:`SvgSaveOptions.resources_folder_alias`"""
        ...
    
    @resource_file_uri.setter
    def resource_file_uri(self, value: str):
        ...
    
    @property
    def keep_resource_stream_open(self) -> bool:
        """Specifies whether Aspose.Words should keep the stream open or close it after saving a resource.
        
        Default is ``False`` and Aspose.Words will close the stream you provided
        in the :attr:`ResourceSavingArgs.resource_stream` property after writing a resource into it.
        Specify ``True`` to keep the stream open."""
        ...
    
    @keep_resource_stream_open.setter
    def keep_resource_stream_open(self, value: bool):
        ...
    
    @property
    def resource_stream(self) -> io.BytesIO:
        """Allows to specify the stream where the resource will be saved to.
        
        This property allows you to save resources to streams instead of files.
        
        The default value is ``None``. When this property is ``None``, the resource
        will be saved to a file specified in the :attr:`ResourceSavingArgs.resource_file_name` property.
        
        Using :class:`IResourceSavingCallback` you cannot substitute one resource with
        another. It is intended only for control over location where to save resources."""
        ...
    
    @resource_stream.setter
    def resource_stream(self, value: io.BytesIO):
        ...
    
    ...

class RtfSaveOptions(aspose.words.saving.SaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.RTF` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.RTF`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def export_compact_size(self) -> bool:
        """Allows to make output RTF documents smaller in size, but if they contain
        RTL (right-to-left) text, it will not be displayed correctly.
        
        Default value is ``False``.
        
        If the document that you want to convert to RTF using Aspose.Words does not contain
        right-to-left text in languages like Arabic, then you can set this option to ``True``
        to reduce the size of the resulting RTF."""
        ...
    
    @export_compact_size.setter
    def export_compact_size(self, value: bool):
        ...
    
    @property
    def export_images_for_old_readers(self) -> bool:
        """Specifies whether the keywords for "old readers" are written to RTF or not.
        This can significantly affect the size of the RTF document.
        
        Default value is ``True``.
        
        "Old readers" are pre-Microsoft Word 97 applications and also WordPad.
        When this option is ``True`` Aspose.Words writes additional RTF keywords.
        These keywords allow the document to be displayed correctly when opened in an
        "old reader" application, but can significantly increase the size of the document.
        
        If you set this option to ``False``, then only images in WMF, EMF and BMP formats
        will be displayed in "old readers"."""
        ...
    
    @export_images_for_old_readers.setter
    def export_images_for_old_readers(self, value: bool):
        ...
    
    @property
    def save_images_as_wmf(self) -> bool:
        """When ``True`` all images will be saved as WMF.
        
        This option might help to avoid WordPad warning messages."""
        ...
    
    @save_images_as_wmf.setter
    def save_images_as_wmf(self, value: bool):
        ...
    
    ...

class SaveOptions:
    """This is an abstract base class for classes that allow the user to specify additional
    options when saving a document into a particular format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article.
    
    An instance of the :class:`SaveOptions` class or any derived class is passed to the stream :meth:`aspose.words.Document.save`
    or string :meth:`aspose.words.Document.save` overloads for the user to define custom options when saving a document."""
    
    @overload
    @staticmethod
    def create_save_options(save_format: aspose.words.SaveFormat) -> aspose.words.saving.SaveOptions:
        """Creates a save options object of a class suitable for the specified save format.
        
        :param save_format: The save format for which to create a save options object.
        :returns: An object of a class that derives from :class:`SaveOptions`."""
        ...
    
    @overload
    @staticmethod
    def create_save_options(file_name: str) -> aspose.words.saving.SaveOptions:
        """Creates a save options object of a class suitable for the file extension specified in the given file name.
        
        :param file_name: The extension of this file name determines the class of the save options object to create.
        :returns: An object of a class that derives from :class:`SaveOptions`."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def export_generator_name(self) -> bool:
        """When ``True``, causes the name and version of Aspose.Words to be embedded into produced files.
        Default value is ``True``."""
        ...
    
    @export_generator_name.setter
    def export_generator_name(self, value: bool):
        ...
    
    @property
    def temp_folder(self) -> str:
        """Specifies the folder for temporary files used when saving to a DOC or DOCX file.
        By default this property is ``None`` and no temporary files are used.
        
        When Aspose.Words saves a document, it needs to create temporary internal structures. By default,
        these internal structures are created in memory and the memory usage spikes for a short period while
        the document is being saved. When saving is complete, the memory is freed and reclaimed by the garbage collector.
        
        Specifying a temporary folder using :attr:`SaveOptions.temp_folder` will cause Aspose.Words to keep the internal structures in
        temporary files instead of memory. It reduces the memory usage during saving, but will decrease the save performance.
        
        The folder must exist and be writable, otherwise an exception will be thrown.
        
        Aspose.Words automatically deletes all temporary files when saving is complete.
        
        :raises RuntimeError (Proxy error(OutOfMemoryException)): Throw if you are saving a very large document (thousands of pages) and/or processing many documents at the same time.
                                                                  The memory spike during saving can be significant enough to cause the exception."""
        ...
    
    @temp_folder.setter
    def temp_folder(self, value: str):
        ...
    
    @property
    def pretty_format(self) -> bool:
        """When ``True``, pretty formats output where applicable.
        Default value is ``False``.
        
        Set to ``True`` to make HTML, MHTML, EPUB, WordML, RTF, DOCX and ODT output human readable.
        Useful for testing or debugging."""
        ...
    
    @pretty_format.setter
    def pretty_format(self, value: bool):
        ...
    
    @property
    def use_anti_aliasing(self) -> bool:
        """Gets or sets a value determining whether or not to use anti-aliasing for rendering.
        
        The default value is ``False``. When this value is set to ``True`` anti-aliasing is
        used for rendering.
        
        This property is used when the document is exported to the following formats:
        :attr:`aspose.words.SaveFormat.TIFF`, :attr:`aspose.words.SaveFormat.PNG`, :attr:`aspose.words.SaveFormat.BMP`,
        :attr:`aspose.words.SaveFormat.JPEG`, :attr:`aspose.words.SaveFormat.EMF`. When the document is exported to the
        :attr:`aspose.words.SaveFormat.HTML`, :attr:`aspose.words.SaveFormat.MHTML`,
        :attr:`aspose.words.SaveFormat.EPUB`, :attr:`aspose.words.SaveFormat.AZW3`
        or :attr:`aspose.words.SaveFormat.MOBI` formats this option is used for raster images."""
        ...
    
    @use_anti_aliasing.setter
    def use_anti_aliasing(self, value: bool):
        ...
    
    @property
    def use_high_quality_rendering(self) -> bool:
        """Gets or sets a value determining whether or not to use high quality (i.e. slow) rendering algorithms.
        
        The default value is ``False``.
        This property is used when the document is exported to image formats:
        :attr:`aspose.words.SaveFormat.TIFF`, :attr:`aspose.words.SaveFormat.PNG`, :attr:`aspose.words.SaveFormat.BMP`,
        :attr:`aspose.words.SaveFormat.JPEG`, :attr:`aspose.words.SaveFormat.EMF`."""
        ...
    
    @use_high_quality_rendering.setter
    def use_high_quality_rendering(self, value: bool):
        ...
    
    @property
    def dml_rendering_mode(self) -> aspose.words.saving.DmlRenderingMode:
        """Gets or sets a value determining how DrawingML shapes are rendered.
        
        The default value is :attr:`DmlRenderingMode.FALLBACK`.
        This property is used when the document is exported to fixed page formats."""
        ...
    
    @dml_rendering_mode.setter
    def dml_rendering_mode(self, value: aspose.words.saving.DmlRenderingMode):
        ...
    
    @property
    def dml_effects_rendering_mode(self) -> aspose.words.saving.DmlEffectsRenderingMode:
        """Gets or sets a value determining how DrawingML effects are rendered.
        
        The default value is :attr:`DmlEffectsRenderingMode.SIMPLIFIED`.
        This property is used when the document is exported to fixed page formats."""
        ...
    
    @dml_effects_rendering_mode.setter
    def dml_effects_rendering_mode(self, value: aspose.words.saving.DmlEffectsRenderingMode):
        ...
    
    @property
    def iml_rendering_mode(self) -> aspose.words.saving.ImlRenderingMode:
        """Gets or sets a value determining how ink (InkML) objects are rendered.
        
        The default value is :attr:`ImlRenderingMode.INK_ML`.
        This property is used when the document is exported to fixed page formats."""
        ...
    
    @iml_rendering_mode.setter
    def iml_rendering_mode(self, value: aspose.words.saving.ImlRenderingMode):
        ...
    
    @property
    def default_template(self) -> str:
        """Gets or sets path to default template (including filename).
        Default value for this property is **empty string** ().
        
        If specified, this path is used to load template when :attr:`aspose.words.Document.automatically_update_styles` is ``True``,
        but :attr:`aspose.words.Document.attached_template` is empty."""
        ...
    
    @default_template.setter
    def default_template(self, value: str):
        ...
    
    @property
    def update_fields(self) -> bool:
        """Gets or sets a value determining if fields of certain types should be updated before saving the document to a fixed page format.
        Default value for this property is ``True``.
        
        Allows to specify whether to mimic or not MS Word behavior."""
        ...
    
    @update_fields.setter
    def update_fields(self, value: bool):
        ...
    
    @property
    def update_last_saved_time_property(self) -> bool:
        """Gets or sets a value determining whether the :attr:`aspose.words.properties.BuiltInDocumentProperties.last_saved_time` property is updated before saving."""
        ...
    
    @update_last_saved_time_property.setter
    def update_last_saved_time_property(self, value: bool):
        ...
    
    @property
    def update_last_printed_property(self) -> bool:
        """Gets or sets a value determining whether the :attr:`aspose.words.properties.BuiltInDocumentProperties.last_printed` property is updated before saving."""
        ...
    
    @update_last_printed_property.setter
    def update_last_printed_property(self, value: bool):
        ...
    
    @property
    def update_created_time_property(self) -> bool:
        """Gets or sets a value determining whether the :attr:`aspose.words.properties.BuiltInDocumentProperties.created_time` property is updated before saving.
        Default value is ``False``;"""
        ...
    
    @update_created_time_property.setter
    def update_created_time_property(self, value: bool):
        ...
    
    @property
    def memory_optimization(self) -> bool:
        """Gets or sets value determining if memory optimization should be performed before saving the document.
        Default value for this property is ``False``.
        
        Setting this option to ``True`` can significantly decrease memory consumption while saving large documents at the cost of slower saving time."""
        ...
    
    @memory_optimization.setter
    def memory_optimization(self, value: bool):
        ...
    
    @property
    def dml_3d_effects_rendering_mode(self) -> aspose.words.saving.Dml3DEffectsRenderingMode:
        """Gets or sets a value determining how 3D effects are rendered.
        
        The default value is :attr:`Dml3DEffectsRenderingMode.BASIC`."""
        ...
    
    @dml_3d_effects_rendering_mode.setter
    def dml_3d_effects_rendering_mode(self, value: aspose.words.saving.Dml3DEffectsRenderingMode):
        ...
    
    @property
    def progress_callback(self) -> aspose.words.saving.IDocumentSavingCallback:
        """Called during saving a document and accepts data about saving progress.
        
        Progress is reported when saving to :attr:`aspose.words.SaveFormat.DOCX`, :attr:`aspose.words.SaveFormat.FLAT_OPC`,
        :attr:`aspose.words.SaveFormat.DOCM`, :attr:`aspose.words.SaveFormat.DOTM`, :attr:`aspose.words.SaveFormat.DOTX`,
        :attr:`aspose.words.SaveFormat.DOC`, :attr:`aspose.words.SaveFormat.DOT`,
        :attr:`aspose.words.SaveFormat.HTML`, :attr:`aspose.words.SaveFormat.MHTML`, :attr:`aspose.words.SaveFormat.EPUB`,
        :attr:`aspose.words.SaveFormat.XAML_FLOW`, or :attr:`aspose.words.SaveFormat.XAML_FLOW_PACK`."""
        ...
    
    @progress_callback.setter
    def progress_callback(self, value: aspose.words.saving.IDocumentSavingCallback):
        ...
    
    @property
    def allow_embedding_post_script_fonts(self) -> bool:
        """Gets or sets a boolean value indicating whether to allow embedding fonts with PostScript outlines
        when embedding TrueType fonts in a document upon it is saved.
        The default value is ``False``.
        
        Note, Word does not embed PostScript fonts, but can open documents with embedded fonts of this type.
        
        This option only works when :attr:`aspose.words.fonts.FontInfoCollection.embed_true_type_fonts` of the
        :attr:`aspose.words.DocumentBase.font_infos` property is set to ``True``."""
        ...
    
    @allow_embedding_post_script_fonts.setter
    def allow_embedding_post_script_fonts(self, value: bool):
        ...
    
    ...

class SaveOutputParameters:
    """This object is returned to the caller after a document is saved and contains additional information that
    has been generated or calculated during the save operation. The caller can use or ignore this object.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article."""
    
    @property
    def content_type(self) -> str:
        """Returns the Content-Type string (Internet Media Type) that identifies the type of the saved document."""
        ...
    
    ...

class SvgSaveOptions(aspose.words.saving.FixedPageSaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.SVG` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.SVG`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def show_page_border(self) -> bool:
        """Controls whether a border is added to the outline of the page.
        Default is ``True``."""
        ...
    
    @show_page_border.setter
    def show_page_border(self, value: bool):
        ...
    
    @property
    def text_output_mode(self) -> aspose.words.saving.SvgTextOutputMode:
        """Gets or sets a value determining how text should be rendered in SVG.
        
        Use this property to get or set the mode of how text inside a document should be rendered
        when saving in SVG format.
        
        The default value is :attr:`SvgTextOutputMode.USE_TARGET_MACHINE_FONTS`."""
        ...
    
    @text_output_mode.setter
    def text_output_mode(self, value: aspose.words.saving.SvgTextOutputMode):
        ...
    
    @property
    def resources_folder(self) -> str:
        """Specifies the physical folder where resources (images) are saved when exporting a document to Svg format.
        Default is ``None``.
        
        Has effect only if :attr:`SvgSaveOptions.export_embedded_images` property is ``False``.
        
        When you save a :class:`aspose.words.Document` in SVG format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`SvgSaveOptions.resources_folder`
        allows you to specify where the images will be saved and :attr:`SvgSaveOptions.resources_folder_alias`
        allows to specify how the image URIs will be constructed.
        
        If you save a document into a file and provide a file name, Aspose.Words, by default, saves the
        images in the same folder where the document file is saved. Use :attr:`SvgSaveOptions.resources_folder`
        to override this behavior.
        
        If you save a document into a stream, Aspose.Words does not have a folder where to save the images,
        but still needs to save the images somewhere. In this case, you need to specify an accessible folder
        in the :attr:`SvgSaveOptions.resources_folder` property"""
        ...
    
    @resources_folder.setter
    def resources_folder(self, value: str):
        ...
    
    @property
    def resources_folder_alias(self) -> str:
        """Specifies the name of the folder used to construct image URIs written into an SVG document.
        Default is ``None``.
        
        When you save a :class:`aspose.words.Document` in SVG format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`SvgSaveOptions.resources_folder`
        allows you to specify where the images will be saved and :attr:`SvgSaveOptions.resources_folder_alias`
        allows to specify how the image URIs will be constructed."""
        ...
    
    @resources_folder_alias.setter
    def resources_folder_alias(self, value: str):
        ...
    
    @property
    def export_embedded_images(self) -> bool:
        """Specified whether images should be embedded into SVG document as base64.
        Note setting this flag can significantly increase size of output SVG file."""
        ...
    
    @export_embedded_images.setter
    def export_embedded_images(self, value: bool):
        ...
    
    @property
    def max_image_resolution(self) -> int:
        """Gets or sets a value in pixels per inch that limits resolution of exported raster images. Default value is zero.
        
        If the value of this property is non-zero, it limits resolution of exported raster images.
        That is, higher-resolution images are resampled down to the limit and lower-resolution images are exported as is.
        
        If the value of this property is zero, all raster images are exported without resampling."""
        ...
    
    @max_image_resolution.setter
    def max_image_resolution(self, value: int):
        ...
    
    @property
    def fit_to_view_port(self) -> bool:
        """Specifies if the output SVG should fill the available viewport area (browser window or container).
        When set to ``True`` width and height of output SVG are set to 100%.
        
        The default value is ``False``."""
        ...
    
    @fit_to_view_port.setter
    def fit_to_view_port(self, value: bool):
        ...
    
    @property
    def resource_saving_callback(self) -> aspose.words.saving.IResourceSavingCallback:
        """Allows to control how resources (images) are saved when a document is exported to SVG format."""
        ...
    
    @resource_saving_callback.setter
    def resource_saving_callback(self, value: aspose.words.saving.IResourceSavingCallback):
        ...
    
    ...

class TxtListIndentation:
    """Specifies how list levels are indented when document is exporting to :attr:`aspose.words.SaveFormat.TEXT` format.
    To learn more, visit the `Save a Document <https://docs.aspose.com/words/python-net/save-a-document/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def count(self) -> int:
        """Gets or sets how many :attr:`TxtListIndentation.character` to use as indentation per one list level.
        The default value is 0, that means no indentation."""
        ...
    
    @count.setter
    def count(self, value: int):
        ...
    
    @property
    def character(self) -> str:
        """Gets or sets which character to use for indenting list levels.
        The default value is '\\0', that means there is no indentation."""
        ...
    
    @character.setter
    def character(self, value: str):
        ...
    
    ...

class TxtSaveOptions(aspose.words.saving.TxtSaveOptionsBase):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.TEXT` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.TEXT`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def simplify_list_labels(self) -> bool:
        """Specifies whether the program should simplify list labels in case of
        complex label formatting not being adequately represented by plain text.
        
        If set to ``True``, numbered list labels are written in simple numeric format
        and itemized list labels as simple ASCII characters. The default value is ``False``."""
        ...
    
    @simplify_list_labels.setter
    def simplify_list_labels(self, value: bool):
        ...
    
    @property
    def add_bidi_marks(self) -> bool:
        """Specifies whether to add bi-directional marks before each BiDi run when exporting in plain text format.
        
        The default value is ``False``."""
        ...
    
    @add_bidi_marks.setter
    def add_bidi_marks(self, value: bool):
        ...
    
    @property
    def list_indentation(self) -> aspose.words.saving.TxtListIndentation:
        """Gets a :class:`TxtListIndentation` object that specifies how many and which character to use for indentation of list levels.
        By default it is zero count of character '\\0', that means no indentation."""
        ...
    
    @property
    def preserve_table_layout(self) -> bool:
        """Specifies whether the program should attempt to preserve layout of tables when saving in the plain text format.
        The default value is ``False``."""
        ...
    
    @preserve_table_layout.setter
    def preserve_table_layout(self, value: bool):
        ...
    
    @property
    def max_characters_per_line(self) -> int:
        """Gets or sets an integer value that specifies the maximum number of characters per one line.
        The default value is 0, that means no limit."""
        ...
    
    @max_characters_per_line.setter
    def max_characters_per_line(self, value: int):
        ...
    
    ...

class TxtSaveOptionsBase(aspose.words.saving.SaveOptions):
    """The base class for specifying additional options when saving a document into a text based formats.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    @property
    def encoding(self) -> str:
        """Specifies the encoding to use when exporting in text formats.
        Default value is **Encoding.UTF8**."""
        ...
    
    @encoding.setter
    def encoding(self, value: str):
        ...
    
    @property
    def paragraph_break(self) -> str:
        """Specifies the string to use as a paragraph break when exporting in text formats.
        
        The default value is :attr:`aspose.words.ControlChar.CR_LF`."""
        ...
    
    @paragraph_break.setter
    def paragraph_break(self, value: str):
        ...
    
    @property
    def force_page_breaks(self) -> bool:
        """Allows to specify whether the page breaks should be preserved during export.
        
        The default value is ``False``.
        
        The property affects only page breaks that are inserted explicitly into a document.
        It is not related to page breaks that MS Word automatically inserts at the end of each page."""
        ...
    
    @force_page_breaks.setter
    def force_page_breaks(self, value: bool):
        ...
    
    @property
    def export_headers_footers_mode(self) -> aspose.words.saving.TxtExportHeadersFootersMode:
        """Specifies the way headers and footers are exported to the text formats.
        Default value is :attr:`TxtExportHeadersFootersMode.PRIMARY_ONLY`."""
        ...
    
    @export_headers_footers_mode.setter
    def export_headers_footers_mode(self, value: aspose.words.saving.TxtExportHeadersFootersMode):
        ...
    
    ...

class WordML2003SaveOptions(aspose.words.saving.SaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.WORD_ML` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article.
    
    At the moment provides only the :attr:`WordML2003SaveOptions.save_format` property, but in the future may have other options added."""
    
    def __init__(self):
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.WORD_ML`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    ...

class XamlFixedSaveOptions(aspose.words.saving.FixedPageSaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.XAML_FIXED` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.XAML_FIXED`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def resources_folder(self) -> str:
        """Specifies the physical folder where resources (images and fonts) are saved when exporting a document to fixed page Xaml format.
        Default is ``None``.
        
        When you save a :class:`aspose.words.Document` in fixed page Xaml format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`XamlFixedSaveOptions.resources_folder`
        allows you to specify where the images will be saved and :attr:`XamlFixedSaveOptions.resources_folder_alias`
        allows to specify how the image URIs will be constructed.
        
        If you save a document into a file and provide a file name, Aspose.Words, by default, saves the
        images in the same folder where the document file is saved. Use :attr:`XamlFixedSaveOptions.resources_folder`
        to override this behavior.
        
        If you save a document into a stream, Aspose.Words does not have a folder where to save the images,
        but still needs to save the images somewhere. In this case, you need to specify an accessible folder
        by using the :attr:`XamlFixedSaveOptions.resources_folder` property"""
        ...
    
    @resources_folder.setter
    def resources_folder(self, value: str):
        ...
    
    @property
    def resources_folder_alias(self) -> str:
        """Specifies the name of the folder used to construct image URIs written into an fixed page Xaml document.
        Default is ``None``.
        
        When you save a :class:`aspose.words.Document` in fixed page Xaml format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`XamlFixedSaveOptions.resources_folder`
        allows you to specify where the images will be saved and :attr:`XamlFixedSaveOptions.resources_folder_alias`
        allows to specify how the image URIs will be constructed."""
        ...
    
    @resources_folder_alias.setter
    def resources_folder_alias(self, value: str):
        ...
    
    @property
    def resource_saving_callback(self) -> aspose.words.saving.IResourceSavingCallback:
        """Allows to control how resources (images and fonts) are saved when a document is exported to fixed page Xaml format."""
        ...
    
    @resource_saving_callback.setter
    def resource_saving_callback(self, value: aspose.words.saving.IResourceSavingCallback):
        ...
    
    ...

class XamlFlowSaveOptions(aspose.words.saving.SaveOptions):
    """Can be used to specify additional options when saving a document into the
    :attr:`aspose.words.SaveFormat.XAML_FLOW` or :attr:`aspose.words.SaveFormat.XAML_FLOW_PACK` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.XAML_FLOW` format."""
        ...
    
    @overload
    def __init__(self, save_format: aspose.words.SaveFormat):
        """Initializes a new instance of this class that can be used to save a document in the :attr:`aspose.words.SaveFormat.XAML_FLOW`
        or :attr:`aspose.words.SaveFormat.XAML_FLOW_PACK` format.
        
        :param save_format: Can be :attr:`aspose.words.SaveFormat.XAML_FLOW` or :attr:`aspose.words.SaveFormat.XAML_FLOW_PACK`."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.XAML_FLOW`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def images_folder(self) -> str:
        """Specifies the physical folder where images are saved when exporting a document to XAML format.
        Default is an empty string.
        
        When you save a :class:`aspose.words.Document` in XAML format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`XamlFlowSaveOptions.images_folder`
        allows you to specify where the images will be saved and :attr:`XamlFlowSaveOptions.images_folder_alias`
        allows to specify how the image URIs will be constructed.
        
        If you save a document into a file and provide a file name, Aspose.Words, by default, saves the
        images in the same folder where the document file is saved. Use :attr:`XamlFlowSaveOptions.images_folder`
        to override this behavior.
        
        If you save a document into a stream, Aspose.Words does not have a folder where to save the images,
        but still needs to save the images somewhere. In this case, you need to specify an accessible folder
        in the :attr:`XamlFlowSaveOptions.images_folder` property or provide custom streams via
        the :attr:`XamlFlowSaveOptions.image_saving_callback` event handler."""
        ...
    
    @images_folder.setter
    def images_folder(self, value: str):
        ...
    
    @property
    def images_folder_alias(self) -> str:
        """Specifies the name of the folder used to construct image URIs written into an XAML document.
        Default is an empty string.
        
        When you save a :class:`aspose.words.Document` in XAML format, Aspose.Words needs to save all
        images embedded in the document as standalone files. :attr:`XamlFlowSaveOptions.images_folder`
        allows you to specify where the images will be saved and :attr:`XamlFlowSaveOptions.images_folder_alias`
        allows to specify how the image URIs will be constructed.
        
        If :attr:`XamlFlowSaveOptions.images_folder_alias` is not an empty string, then the image URI written
        to XAML will be *ImagesFolderAlias + \<image file name\>*.
        
        If :attr:`XamlFlowSaveOptions.images_folder_alias` is an empty string, then the image URI written
        to XAML will be *ImagesFolder + \<image file name\>*.
        
        If :attr:`XamlFlowSaveOptions.images_folder_alias` is set to '.' (dot), then the image file name
        will be written to XAML without path regardless of other options."""
        ...
    
    @images_folder_alias.setter
    def images_folder_alias(self, value: str):
        ...
    
    @property
    def image_saving_callback(self) -> aspose.words.saving.IImageSavingCallback:
        """Allows to control how images are saved when a document is saved to XAML."""
        ...
    
    @image_saving_callback.setter
    def image_saving_callback(self, value: aspose.words.saving.IImageSavingCallback):
        ...
    
    ...

class XlsxSaveOptions(aspose.words.saving.SaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.XLSX`
    format.
    To learn more, visit the `Specify
                Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.XLSX`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def compression_level(self) -> aspose.words.saving.CompressionLevel:
        """Specifies the compression level used to save document.
        The default value is :attr:`CompressionLevel.NORMAL`."""
        ...
    
    @compression_level.setter
    def compression_level(self, value: aspose.words.saving.CompressionLevel):
        ...
    
    @property
    def section_mode(self) -> aspose.words.saving.XlsxSectionMode:
        """Gets or sets the way how sections are handled when saving to the output XLSX document.
        The default value is :attr:`XlsxSectionMode.MULTIPLE_WORKSHEETS`."""
        ...
    
    @section_mode.setter
    def section_mode(self, value: aspose.words.saving.XlsxSectionMode):
        ...
    
    @property
    def date_time_parsing_mode(self) -> aspose.words.saving.XlsxDateTimeParsingMode:
        """Gets or sets the mode that specifies how document text is parsed to identify date and time values.
        The default value is :attr:`XlsxDateTimeParsingMode.USE_CURRENT_LOCALE`."""
        ...
    
    @date_time_parsing_mode.setter
    def date_time_parsing_mode(self, value: aspose.words.saving.XlsxDateTimeParsingMode):
        ...
    
    ...

class XpsSaveOptions(aspose.words.saving.FixedPageSaveOptions):
    """Can be used to specify additional options when saving a document into the :attr:`aspose.words.SaveFormat.XPS` format.
    To learn more, visit the `Specify Save Options <https://docs.aspose.com/words/python-net/specify-save-options/>` documentation article."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of this class that can be used to save a document
        in the :attr:`aspose.words.SaveFormat.XPS` format."""
        ...
    
    @overload
    def __init__(self, save_format: aspose.words.SaveFormat):
        """Initializes a new instance of this class that can be used to save a document
        in the :attr:`aspose.words.SaveFormat.XPS` or :attr:`aspose.words.SaveFormat.OPEN_XPS` format."""
        ...
    
    @property
    def save_format(self) -> aspose.words.SaveFormat:
        """Specifies the format in which the document will be saved if this save options object is used.
        Can only be :attr:`aspose.words.SaveFormat.XPS`."""
        ...
    
    @save_format.setter
    def save_format(self, value: aspose.words.SaveFormat):
        ...
    
    @property
    def outline_options(self) -> aspose.words.saving.OutlineOptions:
        """Allows to specify outline options.
        
        Note that :attr:`OutlineOptions.expanded_outline_levels` option will not work when saving to XPS."""
        ...
    
    @property
    def use_book_fold_printing_settings(self) -> bool:
        """Gets or sets a boolean value indicating whether the document should be saved using a booklet printing layout,
        if it is specified via :attr:`aspose.words.PageSetup.multiple_pages`.
        
        If this option is specified, :attr:`FixedPageSaveOptions.page_set` is ignored when saving.
        This behavior matches MS Word.
        If book fold printing settings are not specified in page setup, this option will have no effect."""
        ...
    
    @use_book_fold_printing_settings.setter
    def use_book_fold_printing_settings(self, value: bool):
        ...
    
    ...

class ColorMode(Enum):
    """Specifies how colors are rendered."""
    
    """Rendering with unmodified colors."""
    NORMAL: int
    
    """Rendering with colors in a range of gray shades from white to black."""
    GRAYSCALE: int
    

class CompressionLevel(Enum):
    """Compression level for OOXML files.
    (DOCX and DOTX files are internally a ZIP-archive, this property controls the compression level of the archive.
    
    Note, that FlatOpc file is not a ZIP-archive, therefore, this property does not affect the FlatOpc files.)"""
    
    """Normal compression level. Default compression level used by Aspose.Words."""
    NORMAL: int
    
    """Maximum compression level."""
    MAXIMUM: int
    
    """Fast compression level."""
    FAST: int
    
    """Super Fast compression level. Microsoft Word uses this compression level."""
    SUPER_FAST: int
    

class CssStyleSheetType(Enum):
    """Specifies how CSS (Cascading Style Sheet) styles are exported to HTML."""
    
    """CSS styles are written inline (as a value of the **style** attribute on every element)."""
    INLINE: int
    
    """CSS styles are written separately from the content in a style sheet embedded in the HTML file."""
    EMBEDDED: int
    
    """CSS styles are written separately from the content in a style sheet in an external file.
    The HTML file links the style sheet."""
    EXTERNAL: int
    

class Dml3DEffectsRenderingMode(Enum):
    """Specifies how 3D shape effects are rendered."""
    
    """A lightweight and stable rendering, based on the internal engine,
    but advanced effects such as lighting, materials and other additional effects
    are not displayed when using this mode.
    Please see documentation for details."""
    BASIC: int
    
    """Rendering of an extended list of special effects including advanced 3D effects
    such as bevels, lighting and materials.
    
    The current implementation uses OpenGL.
    Please make sure that OpenGL library version 1.1 or higher is installed on your system before use.
    This mode is still under development, and some things may not be supported, so it's recommended to use
    the :attr:`Dml3DEffectsRenderingMode.BASIC` mode if the rendering result is not acceptable.
    Please see documentation for details."""
    ADVANCED: int
    

class DmlEffectsRenderingMode(Enum):
    """Specifies how DrawingML effects are rendered to fixed page formats."""
    
    """Rendering of DrawingML effects are simplified."""
    SIMPLIFIED: int
    
    """No DrawingML effects are rendered."""
    NONE: int
    
    """DrawingML effects are rendered in fine mode which involves advanced processing.
    In this mode rendering of effects gives better results but at a higher performance cost than :attr:`DmlEffectsRenderingMode.SIMPLIFIED` mode."""
    FINE: int
    

class DmlRenderingMode(Enum):
    """Specifies how DrawingML shapes are rendered to fixed page formats."""
    
    """If fall-back shape is available for DrawingML, Aspose.Words renders fall-back shape instead of the DrawingML.
    
    Please note that after saving a document to a fixed page format with fall-back DML rendering mode,
    DML shapes in the AW document model are permanently replaced with their fall-back counterparts.
    As a result, saving the same document again will always use fall-back shapes, even if :class:`DmlRenderingMode` is set to :attr:`DmlRenderingMode.DRAWING_ML`."""
    FALLBACK: int
    
    """Aspose.Words ignores fall-back shape of DrawingML and renders DrawingML itself.
    This is the default mode."""
    DRAWING_ML: int
    

class DocumentSplitCriteria(Enum):
    """Specifies how the document is split into parts when saving to :attr:`aspose.words.SaveFormat.HTML`,
    :attr:`aspose.words.SaveFormat.EPUB` or :attr:`aspose.words.SaveFormat.AZW3` format.
    
    :class:`DocumentSplitCriteria` is a set of flags which can be combined. For instance you can split the document
    at page breaks and heading paragraphs in the same export operation.
    
    Different criteria can partially overlap. For instance, **Heading 1** style is frequently given
    :attr:`aspose.words.ParagraphFormat.page_break_before` property so it falls under two criteria: :attr:`DocumentSplitCriteria.PAGE_BREAK` and
    :attr:`DocumentSplitCriteria.HEADING_PARAGRAPH`. Some section breaks can cause page breaks and so on.
    In typical cases specifying only one flag is the most practical option."""
    
    """The document is not split."""
    NONE: int
    
    """The document is split into parts at explicit page breaks.
    A page break can be specified by a :attr:`aspose.words.ControlChar.PAGE_BREAK` character,
    a section break specifying start of new section on a new page,
    or a paragraph that has its :attr:`aspose.words.ParagraphFormat.page_break_before` property set to ``True``."""
    PAGE_BREAK: int
    
    """The document is split into parts at column breaks.
    A column break can be specified by a :attr:`aspose.words.ControlChar.COLUMN_BREAK` character or
    a section break specifying start of new section in a new column."""
    COLUMN_BREAK: int
    
    """The document is split into parts at a section break of any type."""
    SECTION_BREAK: int
    
    """The document is split into parts at a paragraph formatted using a heading style **Heading 1**, **Heading 2** etc.
    Use together with :attr:`HtmlSaveOptions.document_split_heading_level` to specify the heading levels
    (from 1 to the specified level) at which to split."""
    HEADING_PARAGRAPH: int
    

class EmfPlusDualRenderingMode(Enum):
    """Specifies how Aspose.Words should render EMF+ Dual metafiles."""
    
    """Aspose.Words tries to render EMF+ part of EMF+ Dual metafile. If some of the EMF+ records are not supported
    then Aspose.Words renders EMF part of EMF+ Dual metafile."""
    EMF_PLUS_WITH_FALLBACK: int
    
    """Aspose.Words renders EMF+ part of EMF+ Dual metafile."""
    EMF_PLUS: int
    
    """Aspose.Words renders EMF part of EMF+ Dual metafile."""
    EMF: int
    

class ExportFontFormat(Enum):
    """Indicates the format that is used to export fonts while rendering to HTML fixed format."""
    
    """WOFF (Web Open Font Format)."""
    WOFF: int
    
    """TTF (TrueType Font format)."""
    TTF: int
    

class ExportHeadersFootersMode(Enum):
    """Specifies how headers and footers are exported to HTML, MHTML or EPUB."""
    
    """Headers and footers are not exported."""
    NONE: int
    
    """Primary headers and footers are exported at the beginning and the end of each section."""
    PER_SECTION: int
    
    """Primary header of the first section is exported at the beginning of the document and primary footer is at the end."""
    FIRST_SECTION_HEADER_LAST_SECTION_FOOTER: int
    
    """First page header and footer are exported at the beginning and the end of each section."""
    FIRST_PAGE_HEADER_FOOTER_PER_SECTION: int
    

class ExportListLabels(Enum):
    """Specifies how list labels are exported to HTML, MHTML and EPUB."""
    
    """Outputs list labels in auto mode. Uses HTML native elements when possible.
    
    HTML \<ul\> and \<ol\> tags are used for list label representation if it doesn't cause formatting loss, otherwise the HTML \<p\> tag is used."""
    AUTO: int
    
    """Outputs all list labels as inline text.
    
    HTML \<p\> tag is used for any list label representation."""
    AS_INLINE_TEXT: int
    
    """Outputs all list labels as HTML native elements.
    
    HTML \<ul\> and \<ol\> tags are used for list label representation. Some formatting loss is possible."""
    BY_HTML_TAGS: int
    

class HeaderFooterBookmarksExportMode(Enum):
    """Specifies how bookmarks in headers/footers are exported."""
    
    """Bookmarks in headers/footers are not exported."""
    NONE: int
    
    """Only bookmark in first header/footer of the section is exported."""
    FIRST: int
    
    """Bookmarks in all headers/footers are exported."""
    ALL: int
    

class HtmlElementSizeOutputMode(Enum):
    """Specifies how Aspose.Words exports element widths and heights to HTML, MHTML and EPUB."""
    
    """All element sizes, both in absolute and relative units, specified in the document are exported."""
    ALL: int
    
    """Element sizes are exported only if they are specified in relative units in the document.
    Fixed sizes are not exported in this mode. Visual agents will calculate missing sizes to make
    document layout more natural."""
    RELATIVE_ONLY: int
    
    """Element sizes are not exported. Visual agents will build layout automatically according to relationship between elements."""
    NONE: int
    

class HtmlFixedPageHorizontalAlignment(Enum):
    """Specifies the horizontal alignment for pages in output HTML document."""
    
    """Align pages to the left."""
    LEFT: int
    
    """Center pages. This is the default value."""
    CENTER: int
    
    """Align pages to the right."""
    RIGHT: int
    

class HtmlMetafileFormat(Enum):
    """Indicates the format in which metafiles are saved to HTML documents."""
    
    """Metafiles are rendered to raster PNG images."""
    PNG: int
    
    """Metafiles are converted to vector SVG images."""
    SVG: int
    
    """Metafiles are saved as is, without conversion."""
    EMF_OR_WMF: int
    

class HtmlOfficeMathOutputMode(Enum):
    """Specifies how Aspose.Words exports OfficeMath to HTML, MHTML and EPUB."""
    
    """OfficeMath is converted to HTML as image specified by \<img\> tag."""
    IMAGE: int
    
    """OfficeMath is converted to HTML using MathML."""
    MATH_ML: int
    
    """OfficeMath is converted to HTML as sequence of runs specified by \<span\> tags."""
    TEXT: int
    

class HtmlVersion(Enum):
    """Indicates the version of HTML is used when saving the document to :attr:`aspose.words.SaveFormat.HTML` and
    :attr:`aspose.words.SaveFormat.MHTML` formats."""
    
    """Saves the document in compliance with the XHTML 1.0 Transitional standard.
    
    Aspose.Words aims to output XHTML according to the XHTML 1.0 Transitional standard,
    but the output will not always validate against the DTD. Some structures inside a Microsoft Word
    document are hard or impossible to map to a document that will validate against the XHTML schema.
    For example, XHTML does not allow nested lists (UL cannot be nested inside another UL element),
    but in Microsoft Word document multilevel lists occur quite often."""
    XHTML: int
    
    """Saves the document in compliance with the HTML 5 standard."""
    HTML5: int
    

class ImageBinarizationMethod(Enum):
    """Specifies the method used to binarize image."""
    
    """Specifies threshold method."""
    THRESHOLD: int
    
    """Specifies dithering using Floyd-Steinberg error diffusion method."""
    FLOYD_STEINBERG_DITHERING: int
    

class ImageColorMode(Enum):
    """Specifies the color mode for the generated images of document pages."""
    
    """The pages of the document will be rendered as color images."""
    NONE: int
    
    """The pages of the document will be rendered as grayscale images."""
    GRAYSCALE: int
    
    """The pages of the document will be rendered as black and white images."""
    BLACK_AND_WHITE: int
    

class ImagePixelFormat(Enum):
    """Specifies the pixel format for the generated images of document pages."""
    
    """16 bits per pixel, RGB."""
    FORMAT_16BPP_RGB_555: int
    
    """16 bits per pixel, RGB."""
    FORMAT_16BPP_RGB_565: int
    
    """16 bits per pixel, ARGB."""
    FORMAT_16BPP_ARGB_1555: int
    
    """24 bits per pixel, RGB."""
    FORMAT_24BPP_RGB: int
    
    """32 bits per pixel, RGB."""
    FORMAT_32BPP_RGB: int
    
    """32 bits per pixel, ARGB."""
    FORMAT_32BPP_ARGB: int
    
    """32 bits per pixel, ARGB, premultiplied alpha."""
    FORMAT_32BPP_P_ARGB: int
    
    """48 bits per pixel, RGB."""
    FORMAT_48BPP_RGB: int
    
    """64 bits per pixel, ARGB."""
    FORMAT_64BPP_ARGB: int
    
    """64 bits per pixel, ARGB, premultiplied alpha."""
    FORMAT_64BPP_P_ARGB: int
    
    """1 bit per pixel, Indexed."""
    FORMAT_1BPP_INDEXED: int
    

class ImlRenderingMode(Enum):
    """Specifies how ink (InkML) objects are rendered to fixed page formats."""
    
    """If fall-back shape is available for ink (InkML) object, Aspose.Words renders fall-back shape instead of the InkML.
    
    Please note that after saving a document to a fixed page format with fall-back rendering mode,
    InkML objects in the AW document model are permanently replaced with their fall-back counterparts.
    As a result, saving the same document again will always use fall-back shapes, even if :class:`ImlRenderingMode` is set to :attr:`ImlRenderingMode.INK_ML`."""
    FALLBACK: int
    
    """Aspose.Words ignores fall-back shape of ink (InkML) object and renders InkML itself.
    This is the default mode."""
    INK_ML: int
    

class MarkdownLinkExportMode(Enum):
    """Specifies how links are exported into Markdown."""
    
    """Automatically detect export mode for each link."""
    AUTO: int
    
    """Export all links as inline blocks."""
    INLINE: int
    
    """Export all links as reference blocks."""
    REFERENCE: int
    

class MarkdownListExportMode(Enum):
    """Specifies how lists are exported into Markdown."""
    
    """Export list items compatible with Markdown syntax."""
    MARKDOWN_SYNTAX: int
    
    """Export list items as plain text."""
    PLAIN_TEXT: int
    

class MetafileRenderingMode(Enum):
    """Specifies how Aspose.Words should render WMF and EMF metafiles."""
    
    """Aspose.Words tries to render a metafile as vector graphics. If Aspose.Words cannot correctly render some of
    the metafile records to vector graphics then Aspose.Words renders this metafile to a bitmap."""
    VECTOR_WITH_FALLBACK: int
    
    """Aspose.Words renders a metafile as vector graphics."""
    VECTOR: int
    
    """Aspose.Words invokes GDI+ to render a metafile to a bitmap and then saves the bitmap to the output document."""
    BITMAP: int
    

class NumeralFormat(Enum):
    """Indicates the symbol set that is used to represent numbers
    while rendering to fixed page formats."""
    
    """European numerals: 0123456789."""
    EUROPEAN: int
    
    """Numerals used in Arabic: ٠١٢٣٤٥٦٧٨٩.
    Unicode range U+0660 - u+0669."""
    ARABIC_INDIC: int
    
    """Numerals used in Persian and Urdu: ۰۱۲۳۴۵۶۷۸۹.
    Unicode range U+06F0 - u+06F9."""
    EASTERN_ARABIC_INDIC: int
    
    """Symbol set is decided from context(locale and RTL property)."""
    CONTEXT: int
    
    """THIS OPTION IS NOT SUPPORTED.
    Symbol set is decided from regional settings."""
    SYSTEM: int
    

class OdtSaveMeasureUnit(Enum):
    """Specified units of measure to apply to measurable document content such as shape, widths and other during saving."""
    
    """Specifies that the document content is saved using centimeters."""
    CENTIMETERS: int
    
    """Specifies that the document content is saved using inches."""
    INCHES: int
    

class OoxmlCompliance(Enum):
    """Allows to specify which OOXML specification will be used when saving in the DOCX format."""
    
    """ECMA-376 1st Edition, 2006."""
    ECMA376_2006: int
    
    """ISO/IEC 29500:2008 Transitional compliance level."""
    ISO29500_2008_TRANSITIONAL: int
    
    """ISO/IEC 29500:2008 Strict compliance level."""
    ISO29500_2008_STRICT: int
    

class PdfCompliance(Enum):
    """Specifies the PDF standards compliance level."""
    
    """The output file will comply with the PDF 1.7 (ISO 32000-1) standard."""
    PDF17: int
    
    """The output file will comply with the PDF 2.0 (ISO 32000-2) standard."""
    PDF20: int
    
    """The output file will comply with the PDF/A-1a (ISO 19005-1) standard.
    This level includes all the requirements of PDF/A-1b and additionally requires
    that document structure be included (also known as being "tagged"),
    with the objective of ensuring that document content can be searched and repurposed.
    
    Note that exporting the document structure significantly increases the memory consumption, especially
    for the large documents."""
    PDF_A1A: int
    
    """The output file will comply with the PDF/A-1b (ISO 19005-1) standard.
    PDF/A-1b has the objective of ensuring reliable reproduction of the
    visual appearance of the document."""
    PDF_A1B: int
    
    """The output file will comply with the PDF/A-2a (ISO 19005-2) standard.
    This level includes all the requirements of PDF/A-2u and additionally requires
    that document structure be included (also known as being "tagged"),
    with the objective of ensuring that document content can be searched and repurposed.
    
    Note that exporting the document structure significantly increases the memory consumption, especially
    for the large documents."""
    PDF_A2A: int
    
    """The output file will comply with the PDF/A-2u (ISO 19005-2) standard.
    PDF/A-2u has the objective of preserving document static visual appearance over time, independent of the tools
    and systems used for creating, storing or rendering the files. Additionally, any text contained in the document
    can be reliably extracted as a series of Unicode codepoints."""
    PDF_A2U: int
    
    """The output file will comply with the PDF/A-4 (ISO 19005-4:2020) standard.
    PDF/A-4 has the objective of preserving document static visual appearance over time, independent of the tools
    and systems used for creating, storing or rendering the files. Additionally, any text contained in the document
    can be reliably extracted as a series of Unicode codepoints."""
    PDF_A4: int
    
    """The output file will comply with both PDF/A-4 (ISO 19005-4:2020) and PDF/UA-2 (ISO 14289-2:2024) standards.
    PDF/A-4 has the objective of preserving document static visual appearance over time, independent of the tools
    and systems used for creating, storing or rendering the files. The primary purpose of PDF/UA is to define how
    to represent electronic documents in the PDF format in a manner that allows the file to be accessible.
    
    Note that exporting the document structure significantly increases the memory consumption, especially
    for the large documents."""
    PDF_A4_UA_2: int
    
    """The output file will comply with the PDF/UA-1 (ISO 14289-1) standard.
    The primary purpose of PDF/UA is to define how to represent electronic documents in the PDF format in a
    manner that allows the file to be accessible.
    
    Note that exporting the document structure significantly increases the memory consumption, especially
    for the large documents."""
    PDF_UA1: int
    
    """The output file will comply with the PDF/UA-2 (ISO 14289-2:2024) standard.
    The primary purpose of PDF/UA is to define how to represent electronic documents in the PDF format in a
    manner that allows the file to be accessible.
    
    Note that exporting the document structure significantly increases the memory consumption, especially
    for the large documents."""
    PDF_UA2: int
    

class PdfCustomPropertiesExport(Enum):
    """Specifies the way :attr:`aspose.words.Document.custom_document_properties` are exported to PDF file."""
    
    """No custom properties are exported."""
    NONE: int
    
    """Custom properties are exported as entries in /Info dictionary.
    Custom properties with the following names are not exported:
    "Title", "Author", "Subject", "Keywords", "Creator", "Producer", "CreationDate", "ModDate", "Trapped"."""
    STANDARD: int
    
    """Custom properties are Metadata.
    
    The namespace of exported properties in XMP packet is "custprops".
    Every property has an associated xml-element "custprops:Property1", "custprops:Property2" and so on.
    There is "rdf:Description" element inside property element.
    The description element has two elements "custprops:Name", containing custom property's name
    as a value of this xml-element, and "custprops:Value", containing custom property's value as value of this xml-element."""
    METADATA: int
    

class PdfDigitalSignatureHashAlgorithm(Enum):
    """Specifies a digital hash algorithm used by a digital signature."""
    
    """SHA-256 hash algorithm."""
    SHA256: int
    
    """SHA-384 hash algorithm."""
    SHA384: int
    
    """SHA-512 hash algorithm."""
    SHA512: int
    
    """RIPEMD-160 hash algorithm."""
    RIPE_MD160: int
    

class PdfFontEmbeddingMode(Enum):
    """Specifies how Aspose.Words should embed fonts."""
    
    """Aspose.Words embeds all fonts."""
    EMBED_ALL: int
    
    """Aspose.Words embeds all fonts excepting standard Windows fonts Arial and Times New Roman.
    Only Arial and Times New Roman fonts are affected in this mode because MS Word doesn't embed
    only these fonts when saving document to PDF."""
    EMBED_NONSTANDARD: int
    
    """Aspose.Words do not embed any fonts."""
    EMBED_NONE: int
    

class PdfImageColorSpaceExportMode(Enum):
    """Specifies how the color space will be selected for the images in PDF document."""
    
    """Aspose.Words automatically selects the most appropriate color space for each image.
    
    Most of the images are saved in RGB color space. Also Indexed and Grayscale color spaces may be used. CMYK color space is never used.
    
    For some images the color space may be different on different platforms."""
    AUTO: int
    
    """Aspose.Words coverts RGB images to CMYK color space using simple formula.
    
    Images in RGB color space are converted to CMYK using formula:
    Black   = minimum(1-Red,1-Green,1-Blue).
    Cyan    = (1-Red-Black)/(1-Black).
    Magenta = (1-Green-Black)/(1-Black).
    Yellow  = (1-Blue-Black)/(1-Black).
    RGB values are normalized - they are between 0 and 1.0."""
    SIMPLE_CMYK: int
    

class PdfImageCompression(Enum):
    """Specifies the type of compression applied to images in the PDF file."""
    
    """Automatically selects the most appropriate compression for each image."""
    AUTO: int
    
    """Jpeg compression.
    Does not support transparency."""
    JPEG: int
    

class PdfPageLayout(Enum):
    """Specifies the page layout to be used when the document is opened in a PDF reader."""
    
    """Display one page at a time."""
    SINGLE_PAGE: int
    
    """Display the pages in one column."""
    ONE_COLUMN: int
    
    """Display the pages in two columns, with odd-numbered pages on the left."""
    TWO_COLUMN_LEFT: int
    
    """Display the pages in two columns, with odd-numbered pages on the right."""
    TWO_COLUMN_RIGHT: int
    
    """Display the pages two at a time, with odd-numbered pages on the left."""
    TWO_PAGE_LEFT: int
    
    """Display the pages two at a time, with odd-numbered pages on the right."""
    TWO_PAGE_RIGHT: int
    

class PdfPageMode(Enum):
    """Specifies how the PDF document should be displayed when opened in the PDF reader."""
    
    """Neither document outline nor thumbnail images are visible."""
    USE_NONE: int
    
    """Document outline is visible.
    Note that if there're no outlines in the PDF document then outline navigation pane will not be visible anyway."""
    USE_OUTLINES: int
    
    """Thumbnail images are visible."""
    USE_THUMBS: int
    
    """Full-screen mode, with no menu bar, window controls, or any other window visible."""
    FULL_SCREEN: int
    
    """Optional content group panel is visible.
    
    Not supported in the following PDF versions: :attr:`PdfCompliance.PDF_A1A`,
    :attr:`PdfCompliance.PDF_A1B`."""
    USE_OC: int
    
    """Attachments panel is visible.
    
    Not supported in the following PDF versions:  :attr:`PdfCompliance.PDF_A1A`,
    :attr:`PdfCompliance.PDF_A1B`."""
    USE_ATTACHMENTS: int
    

class PdfPermissions(Enum):
    """Specifies the operations that are allowed to a user on an encrypted PDF document."""
    
    """Disallows all operations on the PDF document.
    This is the default value."""
    DISALLOW_ALL: int
    
    """Allows all operations on the PDF document."""
    ALLOW_ALL: int
    
    """Copy or otherwise extract text and graphics from the document by operations other than that controlled
    by :attr:`PdfPermissions.CONTENT_COPY_FOR_ACCESSIBILITY`."""
    CONTENT_COPY: int
    
    """Extract text and graphics (in support of accessibility to users with disabilities or for other purposes)."""
    CONTENT_COPY_FOR_ACCESSIBILITY: int
    
    """Modify the contents of the document by operations other than those controlled by
    :attr:`PdfPermissions.MODIFY_ANNOTATIONS`, :attr:`PdfPermissions.FILL_IN`, and :attr:`PdfPermissions.DOCUMENT_ASSEMBLY`."""
    MODIFY_CONTENTS: int
    
    """Add or modify text annotations, fill in interactive form fields, and, if :attr:`PdfPermissions.MODIFY_CONTENTS` is
    also set, create or modify interactive form fields (including signature fields)."""
    MODIFY_ANNOTATIONS: int
    
    """Fill in existing interactive form fields (including signature fields), even if :attr:`PdfPermissions.MODIFY_CONTENTS`
    is clear."""
    FILL_IN: int
    
    """Assemble the document (insert, rotate, or delete pages and create document outline items or thumbnail
    images), even if :attr:`PdfPermissions.MODIFY_CONTENTS` is clear."""
    DOCUMENT_ASSEMBLY: int
    
    """Print the document (possibly not at the highest quality level, depending on whether
    :attr:`PdfPermissions.HIGH_RESOLUTION_PRINTING` is also set)."""
    PRINTING: int
    
    """Print the document to a representation from which a faithful digital copy of the PDF content could be
    generated, based on an implementation-dependent algorithm. When this flag is clear (and
    :attr:`PdfPermissions.PRINTING` is set), printing shall be limited to a low-level representation of the appearance,
    possibly of degraded quality."""
    HIGH_RESOLUTION_PRINTING: int
    

class PdfTextCompression(Enum):
    """Specifies a type of compression applied to all content in the PDF file except images."""
    
    """No compression."""
    NONE: int
    
    """Flate (ZIP) compression."""
    FLATE: int
    

class PdfZoomBehavior(Enum):
    """Specifies the type of zoom applied to a PDF document when it is opened in a PDF viewer."""
    
    """How the document is displayed is left to the PDF viewer. Usually the viewer displays the document to fit page width."""
    NONE: int
    
    """Displays the page using the specified zoom factor."""
    ZOOM_FACTOR: int
    
    """Displays the page so it visible entirely."""
    FIT_PAGE: int
    
    """Fits the width of the page."""
    FIT_WIDTH: int
    
    """Fits the height of the page."""
    FIT_HEIGHT: int
    
    """Fits the bounding box (rectangle containing all visible elements on the page)."""
    FIT_BOX: int
    

class SvgTextOutputMode(Enum):
    """Allows to specify how text inside a document should be rendered
    when saving in SVG format."""
    
    """SVG fonts are used to render text. Note, not all browsers support SVG fonts."""
    USE_SVG_FONTS: int
    
    """Fonts installed on the target machine are used to render text.
    Note, if some of fonts used in the document are not available on the target machine, document can look differently."""
    USE_TARGET_MACHINE_FONTS: int
    
    """Text is rendered using curves. Note, text selection will not work if you use this option."""
    USE_PLACED_GLYPHS: int
    

class TableContentAlignment(Enum):
    """Allows to specify the alignment of the content of the table to be used when exporting into Markdown format."""
    
    """The alignment will be taken from the first paragraph in corresponding table column."""
    AUTO: int
    
    """The content of tables will be aligned to the Left."""
    LEFT: int
    
    """The content of tables will be aligned to the Center."""
    CENTER: int
    
    """The content of tables will be aligned to the Right."""
    RIGHT: int
    

class TiffCompression(Enum):
    """Specifies what type of compression to apply when saving page images into a TIFF file."""
    
    """Specifies no compression."""
    NONE: int
    
    """Specifies the RLE compression scheme."""
    RLE: int
    
    """Specifies the LZW compression scheme.
    In Java emulated by Deflate (Zip) compression."""
    LZW: int
    
    """Specifies the CCITT3 compression scheme."""
    CCITT3: int
    
    """Specifies the CCITT4 compression scheme."""
    CCITT4: int
    

class TxtExportHeadersFootersMode(Enum):
    """Specifies the way headers and footers are exported to plain text format."""
    
    """No headers and footers are exported."""
    NONE: int
    
    """Only primary headers and footers are exported at the beginning and end of each section.
    
    It is hard to meaningfully output headers and footers to plain text because it is not paginated.
    
    When this mode is used, only primary headers and footers are exported at the beginning and end of each section."""
    PRIMARY_ONLY: int
    
    """All headers and footers are placed after all section bodies at the very end of a document.
    
    This mode is similar to Word."""
    ALL_AT_END: int
    

class XlsxDateTimeParsingMode(Enum):
    """Specifies how document text is parsed to identify date and time values."""
    
    """The datetime format set for the current thread is used first to parse string values. If the parsing fails,
    other common datetime formats are tried."""
    USE_CURRENT_LOCALE: int
    
    """The datetime format used in a document is determined automatically. This may take additional time."""
    AUTO: int
    

class XlsxSectionMode(Enum):
    """Specifies how sections are handled when saving a document in the XLSX format."""
    
    """Specifies that a separate worksheet is created for each section of a document."""
    MULTIPLE_WORKSHEETS: int
    
    """Specifies that all sections of a document are saved on one worksheet."""
    SINGLE_WORKSHEET: int
    

class Zip64Mode(Enum):
    """Specifies when to use ZIP64 format extensions for OOXML files.
    
    OOXML file is a ZIP-archive that has a 4 GB (2^32 bytes) limit on uncompressed size of a file,
    compressed size of a file, and total size of the archive, as well as a limit of 65,535 (2^16-1) files in archive.
    ZIP64 format extensions increase the limits to 2^64."""
    
    """Do not use ZIP64 format extensions."""
    NEVER: int
    
    """If necessary use ZIP64 format extensions."""
    IF_NECESSARY: int
    
    """Always use ZIP64 format extensions."""
    ALWAYS: int
    

